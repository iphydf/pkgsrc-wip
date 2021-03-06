# $NetBSD$

V=		1.6.3
DISTNAME=	libretro-ppsspp-${V}
CATEGORIES=	emulators

HOMEPAGE=	https://docs.libretro.com/library/ppsspp/
COMMENT=	Libretro core based on the PPSSPP PlayStation Portable emulator
LICENSE=	gnu-gpl-v2

ARMIPS_TAG=	8b4cadaf62d7de42d374056fc6aafc555f2bc7dc
GLSLANG_TAG=	2edde6665d9a56ead5ea0e55b4e64d9a803e6164
SPRIV_TAG=	90966d50f57608587bafd95b4e345b02b814754a

DISTFILES+=	ppsspp-${V}.tar.gz
DISTFILES+=	${ARMIPS_TAG}.tar.gz
DISTFILES+=	${GLSLANG_TAG}.tar.gz
DISTFILES+=	${SPRIV_TAG}.tar.gz

SITES.ppsspp-${V}.tar.gz= \
		-${MASTER_SITE_GITHUB:=hrydgard/ppsspp/archive/}v${V}.tar.gz

SITES.${ARMIPS_TAG}.tar.gz= \
		${MASTER_SITE_GITHUB:=Kingcom/armips/archive/}

SITES.${GLSLANG_TAG}.tar.gz= \
		${MASTER_SITE_GITHUB:=hrydgard/glslang/archive/}

SITES.${SPRIV_TAG}.tar.gz= \
		${MASTER_SITE_GITHUB:=KhronosGroup/SPIRV-Cross/archive/}

WRKSRC=		${WRKDIR}/ppsspp-${PKGVERSION_NOREV}
BUILD_DIRS=	libretro

USE_TOOLS+=	gmake pkg-config
USE_LANGUAGES=	c c++
EXTRACT_USING=	bsdtar

.include "../../mk/bsd.fast.prefs.mk"

.if !empty(MACHINE_ARCH:M*arm*)
CFLAGS+=		-marm
BUILD_MAKE_FLAGS+=	TARGET_ARCH=arm
.elif !empty(MACHINE_ARCH:M*x86_64*)
BUILD_MAKE_FLAGS+=	TARGET_ARCH=x86_64
.elif !empty(MACHINE_ARCH:M*i386*)
BUILD_MAKE_FLAGS+=	TARGET_ARCH=x86
.endif

BUILD_MAKE_FLAGS+=	FFMPEGLDFLAGS="`pkg-config --libs libavformat libavcodec libavutil libswresample libswscale`"

INSTALLATION_DIRS+=	${PREFIX}/lib/libretro

post-extract:
	${MV} ${WRKDIR}/armips-${ARMIPS_TAG}/* ${WRKSRC}/ext/armips
	${MV} ${WRKDIR}/glslang-${GLSLANG_TAG}/* ${WRKSRC}/ext/glslang
	${MV} ${WRKDIR}/SPIRV-Cross-${SPRIV_TAG}/* ${WRKSRC}/ext/SPIRV-Cross

do-install:
	${INSTALL_LIB} ${WRKSRC}/libretro/ppsspp_libretro.so \
	    ${DESTDIR}${PREFIX}/lib/libretro/ppsspp_libretro.so

.include "options.mk"

.include "../../mk/dlopen.buildlink3.mk"
BUILDLINK_TRANSFORM+=   opt:-ldl:${BUILDLINK_LDADD.dl:M*}

.include "../../mk/pthread.buildlink3.mk"
.include "../../multimedia/ffmpeg4/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
