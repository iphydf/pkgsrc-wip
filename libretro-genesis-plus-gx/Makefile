# $NetBSD$

DISTNAME=	libretro-genesis-plus-gx-20180218
CATEGORIES=	emulators
MASTER_SITES=	${MASTER_SITE_GITHUB:=libretro/}
GITHUB_PROJECT=	Genesis-Plus-GX
GITHUB_TAG=	6ba9e05419be9aac338e152a9e3fd27b6f3e2297

MAINTAINER=	nia.alarie@gmail.com
HOMEPAGE=	https://docs.libretro.com/library/genesis_plus_gx/
COMMENT=	Libretro core based on the Genesis Plus Sega 8/16 bit emulator
LICENSE=	picodrive-license

EXTRACT_USING=	bsdtar
USE_TOOLS+=	gmake

MAKE_FILE=	Makefile.libretro

MAKE_FLAGS+=	GIT_VERSION="-pkgsrc"
MAKE_FLAGS+=	SHARED_LIBVORBIS=1

.include "../../mk/endian.mk"

.if ${MACHINE_ENDIAN} == "big"
MAKE_FLAGS+=	ENDIANNESS_DEFINES="-DBYTE_ORDER=BIG_ENDIAN -DCPU_IS_BIG_ENDIAN=1 -DWORDS_BIGENDIAN=1"
.endif

INSTALLATION_DIRS+=	${PREFIX}/lib/libretro

do-install:
	${INSTALL_LIB} ${WRKSRC}/genesis_plus_gx_libretro.so \
	    ${DESTDIR}${PREFIX}/lib/libretro/genesis_plus_gx_libretro.so

.include "../../audio/libvorbis/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
