# $NetBSD$

DISTNAME=	neovim-0.2.2
CATEGORIES=	editors
MASTER_SITES=	${MASTER_SITE_GITHUB:=neovim/}
GITHUB_TAG=	v${PKGVERSION_NOREV}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/neovim/neovim/
COMMENT=	Vim-fork focused on extensibility and usability
LICENSE=	apache-2.0 AND vim-license

USE_CMAKE=	yes

USE_LANGUAGES=	c c++

CONFIGURE_DIRS=		${WRKDIR}/build
CMAKE_ARG_PATH=		${WRKSRC}

post-extract:
	${RUN} mkdir -p ${WRKDIR}/build

# should follow the LuaJIT API compatibility
LUA_VERSION_REQD=	51

DEPENDS+=	${LUA_PKGPREFIX}-MessagePack-[0-9]*:../../wip/lua-MessagePack
DEPENDS+=	${LUA_PKGPREFIX}-lpeg-[0-9]*:../../devel/lua-lpeg
DEPENDS+=	${LUA_PKGPREFIX}-mpack-[0-9]*:../../wip/lua-mpack

.include "../../converters/libiconv/buildlink3.mk"
.include "../../devel/jemalloc/buildlink3.mk"
.include "../../devel/libuv/buildlink3.mk"
.include "../../devel/msgpack/buildlink3.mk"
.include "../../lang/lua/application.mk"
.include "../../lang/LuaJIT2/buildlink3.mk"
.include "../../wip/libunibilium/buildlink3.mk"
.include "../../wip/libvterm/buildlink3.mk"
.include "../../wip/libtermkey/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
