# $NetBSD: Makefile,v 1.23 2015/04/25 14:20:40 tnn Exp $
#

DISTNAME=	scintilla375
PKGNAME=	scintilla-3.7.5
#PKGREVISION=	0
CATEGORIES=	devel
MASTER_SITES=	${MASTER_SITE_SOURCEFORGE:=scintilla/}
EXTRACT_SUFX=	.tgz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	http://scintilla.sourceforge.net/
COMMENT=	Source code editing component
LICENSE=	modified-bsd

WRKSRC=		${WRKDIR}/scintilla
USE_LANGUAGES=	c c++
USE_TOOLS+=	gmake pkg-config
BUILD_DIRS=	gtk
MAKE_FILE=	makefile

INSTALLATION_DIRS= include/scintilla lib
do-install:
	${INSTALL_DATA} ${WRKSRC}/include/Scintilla.h \
		${WRKSRC}/include/ScintillaWidget.h \
		${WRKSRC}/include/SciLexer.h \
		${WRKSRC}/include/Platform.h \
		${WRKSRC}/include/Sci_Position.h \
		${WRKSRC}/include/Scintilla.iface \
		${WRKSRC}/include/ILexer.h \
		${DESTDIR}${PREFIX}/include/scintilla
	${INSTALL_LIB} ${WRKSRC}/bin/libscintilla.a ${DESTDIR}${PREFIX}/lib
	${INSTALL_LIB} ${WRKSRC}/bin/libscintilla_lexers.a ${DESTDIR}${PREFIX}/lib


.include "../../x11/gtk2/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
