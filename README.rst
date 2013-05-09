=======================================================================
Owl - The simple configfiles manager
=======================================================================

Imagine a directory like this:

    ~/.owl/
        __me__/
            .vimrc
            .gvimrc
        .hgrc
    /etc/
        httpd/
            httpd.conf

Then you run *owl sync*, and many symlinks are made for you, like this:

    /home/YOU/
        .vimrc  # linking to ~/.owl/.vimrc
        .gvimrc  # linking to ~/.owl/.gvimrc
    /etc/httpd/httpd.conf  # linking to ~/.owl/httpd.conf

Isn't it awesome?


.. .owl/
..     vars.py
..     vars.py.sample  # será clonado para "vars.py" após o download
..     __me__/ <-- considera /home/lsmagalhaes/
..         /.vimrc/
..             (...)
..     /etc
..         /init.d/
..             (...)


.. Usando jinja2, um arquivo vars.py contém as configurações necessárias
.. para setar tudo. Como funcionaria?


.. sintaxe simples para links simbólicos também
.. .vimrc.link
..      e dentro marca o caminho completo de onde o arquivo está



.. OU MELHOR! O owl SÓ FAZ links simbólicos! Uma configuração especial
.. o faz copiar o conteúdo, ao invés de meramente linkar.
