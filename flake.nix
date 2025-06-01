{
  description = "Description for the project";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    systems.url = "github:nix-systems/default";
    fabric = {
      url = "github:Fabric-Development/fabric";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    inputs@{
      self,
      flake-parts,
      systems,
      ...
    }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = import systems;
      perSystem =
        {
          config,
          self',
          inputs',
          pkgs,
          system,
          ...
        }:
        {
          # Define a overlay for fabric so it is accessible from the pkgs attribute set
          _module.args.pkgs = import self.inputs.nixpkgs {
            inherit system;
            overlays = [ (final: prev: { fabric = inputs.fabric.packages.${system}.default; }) ];
          };

          # Defines the package, expects a derivation will be derived via buildPythonApplication
          # https://github.com/NixOS/nixpkgs/blob/master/doc/languages-frameworks/python.section.md
          packages.default = pkgs.python3Packages.buildPythonApplication {
            pname = "stern";
            version = "0.0.1";
            pyproject = true;
            src = ./.;
            doCheck = false;
            dontWrapGApps = true;

            # Native dependencies at build time
            nativeBuildInputs = with pkgs; [
              wrapGAppsHook3
              gtk3
              gobject-introspection
              cairo
            ];

            # Dependencies of the python environment on the
            # target machine.
            dependencies =
              with pkgs.python3Packages;
              [
                python
                setuptools
                wheel
                pip
                pygobject3
                pycairo
              ]
              ++ [ pkgs.fabric ];

            preFixup = ''
              makeWrapperArgs+=("''${gappsWrapperArgs[@]}")
            '';
          };

          apps.default = {
            type = "app";
            program = "${self.packages.${system}.default}/bin/stern";
          };

          # Defines the devshell, expects a derivation which we will derive via mkShell function
          # https://github.com/NixOS/nixpkgs/blob/master/pkgs/build-support/mkshell/default.nix
          devShells.default = pkgs.mkShell {
            name = "stern";
            packages =
              let
                pypkgs = with pkgs.python3Packages; [
                  python
                  setuptools
                  wheel
                  pip
                  pygobject3
                  pycairo
                  loguru
                  pkgconfig
                  python-lsp-server
                ];
              in
              with pkgs;
              [
                fabric
                ruff
                basedpyright
                gtk3
                cairo
                gtk-layer-shell
                gobject-introspection
              ]
              ++ pypkgs;
          };
        };
    };
}
