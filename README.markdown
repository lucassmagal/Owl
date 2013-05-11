Owl - The simple configfiles manager
====================================

Imagine a directory like this:

    ~/.owl/
        __me__/
            .vimrc
            .gvimrc
            .hgrc
    /etc/
        httpd/
            httpd.conf

Then you run **owl sync**, and many symlinks to the readl files
are made for you, like this:

    ~/
        .vimrc  # linking to ~/.owl/__me__/.vimrc
        .gvimrc  # linking to ~/.owl/__me__/.gvimrc
        .hgrc  # and so on
    /etc/httpd/httpd.conf

Isn't it awesome?


<!--

.owl/
    vars.py
    vars.py.sample  # será clonado para "vars.py" após o download
    __me__/ <-- considera /home/lsmagalhaes/
        /.vimrc/
            (...)
    /etc
        /init.d/
            (...)


Usando jinja2, um arquivo vars.py contém as configurações necessárias
para setar tudo. Como funcionaria?


sintaxe simples para links simbólicos também
.vimrc.link
     e dentro marca o caminho completo de onde o arquivo está



OU MELHOR! O owl SÓ FAZ links simbólicos! Uma configuração especial
o faz copiar o conteúdo, ao invés de meramente linkar.

    home/
        __me__/

Outro detalhe: a forma atual de funcionamento impede um "vars.py", pois
tudo funciona na base do symlinking... talvez uma extensão especial, ".template",
ajude. Assim, o linking só é feito quando houver um vars.py local.
-->
