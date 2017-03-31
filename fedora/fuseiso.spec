Summary:	FUSE module to mount ISO filesystem images
Name:		fuseiso
Version:	0.0.0
Release:	0
License:	MIT
Group:		File tools
Url:		git@github.com:megacoder/fuseiso.git

# BuildRequires:	pkgconfig(fuse)
# BuildRequires:	pkgconfig(glib-2.0)
# BuildRequires:	pkgconfig(zlib)
# Requires:	fuse >= 2.2

%description
FuseIso is a FUSE module to mount ISO filesystem images (.iso files,
.bin files, .nrg files..).

The main advantage of using this is that you don't have to be root.

%prep
%setup -q
# %apply_patches
# autoreconf

%build
# export LDFLAGS="`pkg-config glib-2.0 --libs` -lz"
# %configure
# %make

%install
# %makeinstall

%files
%doc AUTHORS COPYING NEWS ChangeLog README
# %{_bindir}/%{name}

