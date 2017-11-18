#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#  Copyright (C) 2017 - Daniele Forghieri
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

"""
Default projects for gtkmm stack
"""

from .utils.base_expanders import Tarball
from .utils.base_expanders import NullExpander
from .utils.base_project import Project
from .utils.base_project import project_add
from .utils.base_builders import Meson

@project_add
class Project_libsigplusplus(Tarball, Meson):
    def __init__(self):
        Project.__init__(self,
            'libsig++',
            archive_url = 'https://download.gnome.org/sources/libsigc++/2.10/libsigc++-2.10.0.tar.xz',
            hash = 'f843d6346260bfcb4426259e314512b99e296e8ca241d771d21ac64f28298d81',
            dependencies = [
                'meson',
                'ninja', 
            ]
        )

    def build(self):
        Meson.build(self)
##?        self.install(r'.\COPYING share\doc\wing')


@project_add
class Project_link_gendef(NullExpander, Meson):
    def __init__(self):
        Project.__init__(self,
            'link-gendef',
            dependencies = [
                'meson',
                'ninja', 
            ]
        )

    def build(self):
        Meson.build(self)
        self.install(r'.\COPYING share\doc\link-gendef')

@project_add
class Project_cairomm(Tarball, Meson):
    def __init__(self):
        Project.__init__(self,
            'cairomm',
            archive_url = 'https://download.gnome.org/sources/cairomm/1.15/cairomm-1.15.4.tar.xz',
            hash = '4cd9fd959538953dfa606aaa7a31381e3193eebf14d814d97ef928684ee9feb5',
            dependencies = [
                'meson',
                'ninja',
                'pkg-config', 
                'libsig++', 
                'link-gendef',
                'cairo', 
            ],
            patches = [
                '001-define-mpi-msvc.patch',
            ],
        )

@project_add
class Project_glibmm(Tarball, Meson):
    def __init__(self):
        Project.__init__(self,
            'glibmm',
            archive_url = 'https://download.gnome.org/sources/glibmm/2.54/glibmm-2.54.1.tar.xz',
            hash = '7cc28c732b04d70ed34f0c923543129083cfb90580ea4a2b4be5b38802bf6a4a',
            dependencies = [ 
                'libsig++', 
                'glib', 
            ],
        )

@project_add
class Project_pangomm(Tarball, Meson):
    def __init__(self):
        Project.__init__(self,
            'pangomm',
            archive_url = 'https://download.gnome.org/sources/pangomm/2.40/pangomm-2.40.1.tar.xz',
            hash = '9762ee2a2d5781be6797448d4dd2383ce14907159b30bc12bf6b08e7227be3af',
            dependencies = [ 
                'libsig++', 
                'pango', 
                'cairomm', 
                'glibmm', 
            ],
        )

@project_add
class Project_atkmm(Tarball, Meson):
    def __init__(self):
        Project.__init__(self,
            'atkmm',
            archive_url = 'https://download.gnome.org/sources/atkmm/2.24/atkmm-2.24.2.tar.xz',
            hash = 'ff95385759e2af23828d4056356f25376cfabc41e690ac1df055371537e458bd',
            dependencies = [ 
                'libsig++', 
                'atk', 
                'glibmm', 
            ],
        )

@project_add
class Project_gtkmm(Tarball, Meson):
    def __init__(self):
        Project.__init__(self,
            'gtkmm',
            archive_url = 'https://download.gnome.org/sources/gtkmm/3.22/gtkmm-3.22.2.tar.xz',
            hash = '91afd98a31519536f5f397c2d79696e3d53143b80b75778521ca7b48cb280090',
            dependencies = [ 
                'libsig++', 
                'gtk', 
                'atkmm', 
                'pangomm', 
            ],
        )
