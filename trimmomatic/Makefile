# $NetBSD$

DISTNAME=	Trimmomatic-${PORTVERSION}
CATEGORIES=	biology
MASTER_SITES=	http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/
EXTRACT_SUFX=	.zip

MAINTAINER=	bacon@NetBSD.org
HOMEPAGE=	http://www.usadellab.org/cms/?page=trimmomatic
COMMENT=	Flexible read trimming tool for Illumina NGS data
LICENSE=	gnu-gpl-v3

# FIXME: Should at least error out if no jvm available on Linux
USE_JAVA=	run

USE_TOOLS+=	pax
NO_BUILD=	yes

WRKSRC=		${WRKDIR}/Trimmomatic-${PORTVERSION}

PORTVERSION=	0.35
DATADIR=	${PREFIX}/share/trimmomatic

INSTALLATION_DIRS=	lib/java share/trimmomatic

do-install:
	${INSTALL_DATA} ${WRKSRC}/trimmomatic-0.35.jar ${DESTDIR}${PREFIX}/lib/java/trimmomatic.jar
	cd ${WRKSRC} && pax -rw adapters ${DESTDIR}${DATADIR}

.include "../../mk/bsd.pkg.mk"
