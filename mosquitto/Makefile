# $NetBSD$

DISTNAME=	mosquitto-${VERSION}
VERSION=	1.4.15
CATEGORIES=	net
MASTER_SITES=	http://mosquitto.org/files/source/

MAINTAINER=	amoibos@gmail.com
HOMEPAGE=	http://mosquitto.org/
COMMENT=	Open Source MQTT broker
LICENSE=	epl-v1.0

USE_LANGUAGES+=	c c++
USE_TOOLS+=	cmake gmake

TEST_TARGET=	test

CONF_FILES=	share/examples/mosquitto/pskfile.example \
		share/examples/mosquitto/pwfile.example \
		share/examples/mosquitto/mosquitto.conf \
		share/examples/mosquitto/aclfile.example

post-install:
	mkdir ${DESTDIR}${PREFIX}/share/examples/mosquitto
	${INSTALL_DATA}	${WRKSRC}/pskfile.example ${WRKSRC}/pwfile.example ${WRKSRC}/mosquitto.conf ${WRKSRC}/aclfile.example ${DESTDIR}${PREFIX}/share/examples/mosquitto

.include "../../net/libcares/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
