#!/usr/bin/env bash

set -e

export FORCE_COLOR=1

say () {
    {
        printf "[SmartPyInstaller] "
        printf "$@"
        printf "\n"
    } >&2
}

export smartml_app_name=install.sh
install_path=$(dirname "$0")
export smartpy_install_path="$install_path"

usage () {
    cat >&2 <<EOF
[SmartPyInstaller]

See introduction: https://smartpy-io.medium.com/f5bd8772b74a

Install directory: $install_path

Usage: $(basename $0) <command> <arguments>

- local-install PATH                   : Install the default version of SmartPy at PATH.
- local-install-custom DISTRIB PATH    : Like local-install but get the 'DISTRIB' version.
- local-install-from SRC-PATH DST-PATH :
  Install from another installation, or from the git repository's python/
  directory.

EOF
}

download () {
    local uri="$1"
    local out="$2"
    say "Downloading $uri to $out ..."
    if [ -f "$out" ] ; then
        rm "$out"
    fi
    curl --fail --show-error -s "$uri" > "$out"
    if [ -f "$out" ] ; then
        :
    else
        say "Download of '$uri' failed"
        exit 4
    fi
}

files_to_install="
SmartPy.sh
browser.py
install.sh
originator.js
smart-ts-cli.js
smart.css
smart.js
smartml_cli.tar.gz
smartpy.py
smartpyc.js
smartpyc.py
smartpyio.py
smarttop
templates/welcome.py
theme.js
typography.css
"

install_from () {
    local method="$1"
    local from="$2"
    local path="$3"
    local smartml="$4"

    if [ "$path" = "" ]; then
        echo "Install in default directory: ~/smartpy-cli ? [y/N] "
        read default_install
        if [ "$default_install" = "y" ]; then
            path=~/smartpy-cli
        else
            echo "Cancelling"
            exit 1
        fi
    fi

    if [ -d "$path" ]; then
        echo "Directory ${path} already exists."
        echo "Files will be directly created in ${path}; overwrite ? [y/N] "
        read overwrite
        if [ "$overwrite" != "y" ]; then
            echo "Cancelling"
            exit 1
        fi
    fi

    mkdir -p $path/templates
    for f in $files_to_install ; do
        $method "$from/$f" "$path/$f"
    done
    if [ "$native" = "1" ]; then
        $method "$from/smartpyc" "$path/smartpyc"
        chmod +x "$path/smartpyc"
    fi
    ( cd "$path" ;
      npm init --yes > /dev/null ;
      npm install libsodium-wrappers-sumo bs58check js-sha3 tezos-bls12-381 chalk @smartpy/originator @smartpy/timelock;
    )

    if [ "$smartml" == "smartml" ]; then
        (
            cd "$path"
            rm -rf smartml_cli driver.exe
            tar -xvf smartml_cli.tar.gz
            opam switch -y remove smartML-local || true
            opam switch create smartML-local ocaml-base-compiler.4.10.2
            eval $(cd ~/.opam/smartML-local; opam env)
            opam install -y \
              ocamlfind \
              smartml_cli/utils_pure/utils_pure.opam \
              smartml_cli/michelson_base/michelson_base.opam \
              smartml_cli/core/smartML.opam \
              smartml_cli/ppx_smartml/ppx_smartml_lib.opam \
              smartml_cli/ppx_smartml/driver.opam
            ocamlfind ocamlmktop -o smarttop.exe -package num,utils_pure,smartML -linkpkg
            ln -s ~/.opam/smartML-local/bin/driver driver.exe
            chmod +x smarttop smarttop.exe
        )
    fi

    chmod +x "$path/SmartPy.sh" "$path/originator.js"
    say "Installation successful in $path"
}

native=0
for var in "$@"
do
    case "$var" in
        "--native")
            native=1;;
        * )
        ;;
    esac
done

case "$1" in
    "help" | "--help" | "-h")
        usage ;;
    "" | "local-install" | "--native")
        install_from download https://smartpy.io/cli "$2" "";;
    "--with_smartml")
        install_from download https://smartpy.io/cli "$2" "smartml";;
    "local-install-custom" )
        install_from download "$2" "$3" "";;
    "local-install-from" )
        shift
        install_from cp "$1" "$2" "";;
    "local-install-from-smartml" )
        shift
        install_from cp "$1" "$2" "smartml";;
    * )
        usage
        ;;
esac
