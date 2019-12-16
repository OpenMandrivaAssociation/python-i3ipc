Name:           python-i3ipc
Version:        1.5.1
Release:        1
Summary:        An improved Python library to control i3wm
License:        BSD
URL:            https://github.com/acrisci/i3ipc-python
BuildArch:      noarch
Source0:        https://github.com/acrisci/i3ipc-python/archive/v%{version}.tar.gz
# https://github.com/acrisci/i3ipc-python/pull/76
Patch0:         0001-Adapt-test-launcher-for-our-envirnoment.patch

BuildRequires:  pkgconfig(python)

%global desc \
i3's interprocess communication (or ipc) is the interface i3wm uses to receive\
commands from client applications such as i3-msg. It also features\
a publish/subscribe mechanism for notifying interested parties of window\
manager events.\
\
i3ipc-python is a Python library for controlling the window manager. This\
project is intended to be useful for general scripting, and for applications\
that interact with the window manager like status line generators, notification\
daemons, and pagers.\

%description
%{desc}

%prep
%setup -q -n i3ipc-python-%{version}
%autopatch -p1

sed -i '/^#!/d' i3ipc/i3ipc.py

%build
%py3_build

%install
%py3_install

%files
%{python3_sitelib}/*
%license LICENSE
%doc README.rst
