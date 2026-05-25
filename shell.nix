
{ pkgs ? import <nixpkgs> {} }:

let
  # On ajoute ici toutes les bibliothèques système + graphiques requises par SDL2/Pygame
  libraries = with pkgs; [
    stdenv.cc.cc.lib
    zlib
    glib
    libffi
    
    libGL          
    wayland        
    libx11    
    libxext
    libxrender
    libxrandr
    libxcursor
    libxi
    libxinerama
    libxscrnsaver
  ];
in
pkgs.mkShell {
  buildInputs = [
    pkgs.python313
    pkgs.poetry
  ] ++ libraries;

  shellHook = ''
    export POETRY_VIRTUALENVS_IN_PROJECT=true

    # Met à jour le LD_LIBRARY_PATH pour que Python trouve les fichiers .so graphiques
    export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath libraries}:$LD_LIBRARY_PATH"

    poetry install
    source .venv/bin/activate
    pycharm > /dev/null 2>&1 &

    echo "Nix-shell OK"
  '';
}
