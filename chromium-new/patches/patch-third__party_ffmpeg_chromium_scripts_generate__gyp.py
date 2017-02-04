$NetBSD$

--- third_party/ffmpeg/chromium/scripts/generate_gyp.py.orig	2016-11-10 20:02:58.000000000 +0000
+++ third_party/ffmpeg/chromium/scripts/generate_gyp.py
@@ -43,6 +43,8 @@ import sys
 COPYRIGHT = """# Copyright %d The Chromium Authors. All rights reserved.
 # Use of this source code is governed by a BSD-style license that can be
 # found in the LICENSE file.
+#
+# modified: cmt@burggraben.net
 
 # NOTE: this file is autogenerated by ffmpeg/chromium/scripts/generate_gyp.py
 
@@ -372,6 +374,8 @@ class SourceSet(object):
 
       if condition.PLATFORM == '*':
         platform_condition = None
+      elif condition.PLATFORM == 'linux':
+        platform_condition = '(OS == "%s" or os_bsd == 1)' % condition.PLATFORM
       else:
         platform_condition = 'OS == "%s"' % condition.PLATFORM
 