# $NetBSD$

BUILDLINK_TREE+=	uthash

.if !defined(UTHASH_BUILDLINK3_MK)
UTHASH_BUILDLINK3_MK:=

BUILDLINK_API_DEPENDS.uthash+=	uthash>=1.9.9
BUILDLINK_PKGSRCDIR.uthash?=	../../wip/uthash
BUILDLINK_DEPMETHOD.uthash?=	build
.endif	# UTHASH_BUILDLINK3_MK

BUILDLINK_TREE+=	-uthash
