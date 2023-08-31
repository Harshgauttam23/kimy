[app]

# (str) Title of your application
title = YourAppTitle

# (str) Package name
package.name = yourapppackage

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,json

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude
source.exclude_dirs = tests, __pycache__

# (str) Application versioning (method to update the version string)
version.regex = __version__ = ['"](.*)['"]
version.filename = main.py

# (str) Android/IOS version
osx.python_version = 3.7.9

# (list) Permissions
android.permissions = INTERNET

# (list) Gradle dependencies
android.gradle_dependencies = com.google.guava:guava:29.0-android

# (list) Android-specific parameters
android.api = 28
android.minapi = 21
android.sdk = 28

# (str) iOS SDK version (xcode)
ios.sdk = 14.5

# (list) iOS frameworks to link against
ios.frameworks = UIKit

# (list) iOS plist entries
ios.plist_entries = NSCameraUsageDescription = Use the camera to take photos

# (list) Application requirements
requirements = kivy==2.0.0,kivymd==0.104.1,gspread

# (str) Presplash of the application
presplash.filename = path/to/presplash.png

# (str) Icon of the application
icon.filename = path/to/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (str) Android logcat filters
logcat_filters = *:S python:D

# (bool) If true, then the keyboard will not dismiss when clicking outside the Textinput widget.
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-XXXXXXXXXXXXXXXX~XXXXXXXXXX
