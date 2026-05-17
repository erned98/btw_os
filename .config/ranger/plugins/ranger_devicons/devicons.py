#!/usr/bin/python
# coding=UTF-8

import os

# Unified, single-cell icon theme for ranger.
# Primary style: Font Awesome (nf-fa) where practical, with a few close Nerd Font
# fallbacks when nf-fa lacks a clear one-cell equivalent.

xdgs_dirs = {
    os.path.basename(os.getenv(key).rstrip('/')): icon
    for key, icon in (
        ('XDG_DOCUMENTS_DIR', ''),
        ('XDG_DOWNLOAD_DIR', ''),
        ('XDG_CONFIG_DIR', ''),
        ('XDG_MUSIC_DIR', ''),
        ('XDG_PICTURES_DIR', ''),
        ('XDG_PUBLICSHARE_DIR', ''),
        ('XDG_TEMPLATES_DIR', ''),
        ('XDG_VIDEOS_DIR', ''),
    )
    if os.getenv(key)
}

file_node_extensions = {
    '7z': '', 'a': '', 'ai': '', 'apk': '', 'asm': '', 'asp': '',
    'aup': '', 'avi': '', 'awk': '', 'bash': '', 'bat': '', 'bmp': '',
    'bz2': '', 'c': '', 'c++': '', 'cab': '', 'cbr': '', 'cbz': '',
    'cc': '', 'class': '', 'clj': '', 'cljc': '', 'cljs': '', 'cmake': '',
    'coffee': '', 'conf': '', 'cp': '', 'cpio': '', 'cpp': '', 'cs': '',
    'csh': '', 'css': '', 'cue': '', 'cvs': '', 'cxx': '', 'd': '',
    'dart': '', 'db': '', 'deb': '', 'diff': '', 'dll': '',
    'doc': '', 'docm': '', 'docx': '', 'dotm': '', 'dotx': '',
    'dps': '', 'dpt': '', 'dump': '', 'edn': '', 'eex': '', 'efi': '',
    'ejs': '', 'elf': '', 'elm': '', 'epub': '', 'erl': '', 'ex': '',
    'exe': '', 'exs': '', 'f#': '', 'fifo': '', 'fish': '', 'flac': '',
    'flv': '', 'fs': '', 'fsi': '', 'fsscript': '', 'fsx': '', 'gem': '',
    'gemspec': '', 'gif': '', 'go': '', 'gz': '', 'gzip': '', 'h': '',
    'haml': '', 'hbs': '', 'hh': '', 'hpp': '', 'hrl': '', 'hs': '',
    'htaccess': '', 'htm': '', 'html': '', 'htpasswd': '', 'hxx': '',
    'ico': '', 'img': '', 'ini': '', 'ipynb': '', 'iso': '', 'jar': '',
    'java': '', 'jl': '', 'jpeg': '', 'jpg': '', 'js': '', 'json': '',
    'jsonc': '', 'jsx': '', 'key': '', 'ksh': '', 'leex': '', 'less': '',
    'lha': '', 'lhs': '', 'log': '', 'lua': '', 'lz': '', 'lzh': '',
    'lzma': '', 'm4a': '', 'm4v': '', 'markdown': '', 'md': '',
    'mdx': '', 'mjs': '', 'mka': '', 'mkv': '', 'ml': '', 'mli': '',
    'mov': '', 'mp3': '', 'mp4': '', 'mpeg': '', 'mpg': '', 'msi': '',
    'mustache': '', 'nix': '', 'o': '', 'ogg': '', 'opus': '', 'part': '',
    'pdf': '', 'php': '', 'pl': '', 'pm': '', 'png': '', 'pot': '',
    'potm': '', 'potx': '', 'pp': '', 'pps': '', 'ppsm': '', 'ppsx': '',
    'ppt': '', 'pptm': '', 'pptx': '', 'procfile': '', 'ps1': '',
    'psb': '', 'psd': '', 'pub': '', 'py': '', 'pyc': '', 'pyd': '',
    'pyo': '', 'r': '', 'rake': '', 'rar': '', 'rb': '', 'rc': '',
    'rlib': '', 'rmd': '', 'rom': '', 'rpm': '', 'rproj': '', 'rs': '',
    'rss': '', 'rtf': '', 's': '', 'sass': '', 'scala': '', 'scss': '',
    'sh': '', 'slim': '', 'sln': '', 'so': '', 'sql': '', 'styl': '',
    'suo': '', 'svelte': '', 'swift': '', 't': '', 'tar': '', 'tex': '',
    'tgz': '', 'toml': '', 'torrent': '', 'ts': '', 'tsx': '', 'twig': '',
    'vim': '', 'vimrc': '', 'vue': '', 'wav': '', 'webm': '',
    'webmanifest': '', 'webp': '', 'wps': '', 'wpt': '', 'xbps': '',
    'xcplayground': '', 'xhtml': '', 'xla': '', 'xlam': '', 'xls': '',
    'xlsb': '', 'xlsm': '', 'xlsx': '', 'xlt': '', 'xltm': '',
    'xltx': '', 'xml': '', 'xul': '', 'xz': '', 'yaml': '', 'yml': '',
    'zip': '', 'zsh': '', 'txt': '', 'text': '', 'rst': ''
}

dir_node_exact_matches = {
    '.git': '', 'Desktop': '', 'Documents': '', 'Downloads': '',
    'Dotfiles': '', 'Dropbox': '', 'Music': '', 'Pictures': '',
    'Public': '', 'Templates': '', 'Videos': '', 'anaconda3': '',
    'go': '', 'workspace': '', 'OneDrive': '',
    'Escritorio': '', 'Documentos': '', 'Descargas': '', 'Música': '',
    'Imágenes': '', 'Público': '', 'Plantillas': '', 'Vídeos': '',
    'Bureau': '', 'Images': '', 'Musique': '', 'Publique': '',
    'Téléchargements': '', 'Vidéos': '',
    'Imagens': '', 'Modelos': '', 'Área de trabalho': '',
    'Documenti': '', 'Immagini': '', 'Modelli': '', 'Musica': '',
    'Pubblici': '', 'Scaricati': '', 'Scrivania': '', 'Video': '',
    'Bilder': '', 'Dokumente': '', 'Musik': '', 'Schreibtisch': '',
    'Vorlagen': '', 'Öffentlich': '',
    'Dokumentumok': '', 'Képek': '', 'Zene': '', 'Letöltések': '',
    'Számítógép': '', 'Videók': '',
    '桌面': '', '文档': '', '下载': '', '音乐': '', '图片': '',
    '公共的': '', '公共': '', '模板': '', '视频': '',
    '文檔': '', '下載': '', '音樂': '', '圖片': '', '視頻': '',
    'Skrivbord': '', 'Dokument': '', 'Hämtningar': '', 'Mallar': '',
    'Pulpit': '', 'Dokumenty': '', 'Pobrane': '', 'Muzyka': '',
    'Obrazy': '', 'Publiczne': '', 'Szablony': '', 'Wideo': ''
}

dir_node_exact_matches.update(xdgs_dirs)

file_node_exact_matches = {
    '.bash_aliases': '', '.bash_history': '', '.bash_logout': '',
    '.bash_profile': '', '.bashprofile': '', '.bashrc': '', '.dmrc': '',
    '.DS_Store': '', '.fasd': '', '.fehbg': '', '.gitattributes': '',
    '.gitconfig': '', '.gitignore': '', '.gitlab-ci.yml': '', '.gvimrc': '',
    '.inputrc': '', '.jack-settings': '', '.mime.types': '', '.ncmpcpp': '',
    '.nvidia-settings-rc': '', '.pam_environment': '', '.profile': '',
    '.recently-used': '', '.selected_editor': '', '.vim': '', '.viminfo': '',
    '.vimrc': '', '.Xauthority': '', '.Xdefaults': '', '.xinitrc': '',
    '.xinputrc': '', '.Xresources': '', '.zshrc': '', '_gvimrc': '',
    '_vimrc': '', 'a.out': '', 'authorized_keys': '', 'bspwmrc': '',
    'cmakelists.txt': '', 'config': '', 'config.ac': '', 'config.m4': '',
    'config.mk': '', 'config.ru': '', 'configure': '',
    'docker-compose.yml': '', 'dockerfile': '', 'Dockerfile': '',
    'dropbox': '', 'favicon.ico': '', 'gemfile': '',
    'gruntfile.coffee': '', 'gruntfile.js': '', 'gruntfile.ls': '',
    'gulpfile.coffee': '', 'gulpfile.js': '', 'gulpfile.ls': '', 'ini': '',
    'known_hosts': '', 'ledger': '', 'license': '', 'LICENSE': '',
    'LICENSE.md': '', 'LICENSE.txt': '', 'Makefile': '', 'makefile': '',
    'Makefile.ac': '', 'Makefile.in': '', 'mimeapps.list': '',
    'mix.lock': '', 'node_modules': '', 'package-lock.json': '',
    'package.json': '', 'playlists': '', 'procfile': '', 'Rakefile': '',
    'rakefile': '', 'react.jsx': '', 'README': '', 'README.markdown': '',
    'README.md': '', 'README.rst': '', 'README.txt': '', 'sxhkdrc': '',
    'user-dirs.dirs': '', 'webpack.config.js': ''
}


def devicon(file):
    if file.is_directory:
        return dir_node_exact_matches.get(file.relative_path, '')
    return file_node_exact_matches.get(
        os.path.basename(file.relative_path),
        file_node_extensions.get(file.extension, '')
    )
