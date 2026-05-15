{ pkgs ? import <nixpkgs> {} }:

let
  # On définit une liste des bibliothèques souvent nécessaires
  libraries = with pkgs; [
    stdenv.cc.cc.lib
    zlib
    glib
    libffi
  ];
in
pkgs.mkShell {
  buildInputs = [
    pkgs.python313
    pkgs.poetry
  ] ++ libraries;

  shellHook = ''
    export POETRY_VIRTUALENVS_IN_PROJECT=true

    export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath libraries}:$LD_LIBRARY_PATH"

    poetry install
    source .venv/bin/activate
    pycharm > /dev/null 2>&1 &

    echo "Nix-shell OK"
  '';
}
