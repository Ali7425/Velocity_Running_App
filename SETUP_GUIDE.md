# iOS and Android Setup Guide for Velocity Running App

This guide outlines all the requirements and steps needed to finish the setup for both iOS and Android app initialization.

## ✅ Already Configured

- Basic Expo configuration
- App icons and splash screen
- React Native Maps dependency
- Expo Router setup

## 📋 Required Configuration Updates

### 1. App.json Configuration

The `app.json` has been updated with:
- **iOS**: Bundle identifier, build number, deployment target, location permissions
- **Android**: Package name, version code, location permissions

### 2. React Native Maps Setup

Since your app uses `react-native-maps`, you need to configure API keys:

#### For iOS:
1. Get a Google Maps API key from [Google Cloud Console](https://console.cloud.google.com/)
2. Enable "Maps SDK for iOS"
3. Add the API key to `app.json`:

```json
"ios": {
  "config": {
    "googleMapsApiKey": "YOUR_IOS_API_KEY_HERE"
  }
}
```

#### For Android:
1. Get a Google Maps API key from [Google Cloud Console](https://console.cloud.google.com/)
2. Enable "Maps SDK for Android"
3. Add the API key to `app.json`:

```json
"android": {
  "config": {
    "googleMapsApiKey": "YOUR_ANDROID_API_KEY_HERE"
  }
}
```

## 🛠️ Development Environment Setup

### For iOS Development:

#### Prerequisites:
1. **macOS** (required for iOS development)
2. **Xcode** (latest version from App Store)
3. **Xcode Command Line Tools**:
   ```bash
   xcode-select --install
   ```
4. **CocoaPods** (for iOS dependencies):
   ```bash
   sudo gem install cocoapods
   ```

#### Setup Steps:
1. Install dependencies:
   ```bash
   npm install
   ```

2. Generate native iOS project (if you need native code customization):
   ```bash
   npx expo prebuild --platform ios
   ```

3. Install iOS pods:
   ```bash
   cd ios && pod install && cd ..
   ```

4. Start the development server:
   ```bash
   npm run ios
   ```
   or
   ```bash
   npx expo start --ios
   ```

### For Android Development:

#### Prerequisites:
1. **Java Development Kit (JDK)** - Version 17 or later
   - Check: `java -version`
   - Install via Homebrew: `brew install openjdk@17`

2. **Android Studio** (latest version)
   - Download from [developer.android.com](https://developer.android.com/studio)
   - Install Android SDK, Android SDK Platform, and Android Virtual Device

3. **Android SDK**:
   - Open Android Studio → SDK Manager
   - Install Android SDK Platform 34 (or latest)
   - Install Android SDK Build-Tools
   - Install Android Emulator

4. **Environment Variables** (add to `~/.zshrc` or `~/.bash_profile`):
   ```bash
   export ANDROID_HOME=$HOME/Library/Android/sdk
   export PATH=$PATH:$ANDROID_HOME/emulator
   export PATH=$PATH:$ANDROID_HOME/platform-tools
   export PATH=$PATH:$ANDROID_HOME/tools
   export PATH=$PATH:$ANDROID_HOME/tools/bin
   ```

5. **Reload shell configuration**:
   ```bash
   source ~/.zshrc
   ```

#### Setup Steps:
1. Install dependencies:
   ```bash
   npm install
   ```

2. Generate native Android project (if you need native code customization):
   ```bash
   npx expo prebuild --platform android
   ```

3. Start the development server:
   ```bash
   npm run android
   ```
   or
   ```bash
   npx expo start --android
   ```

## 🚀 Quick Start (Using Expo Go - No Native Setup Required)

If you just want to test the app quickly without setting up native development:

1. Install Expo Go app on your iOS/Android device
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```
4. Scan the QR code with Expo Go app

**Note**: Some features (like native maps) may have limited functionality in Expo Go.

## 📱 Building for Production

### iOS Build:
1. Ensure you have an Apple Developer account
2. Configure signing in Xcode
3. Build:
   ```bash
   npx expo build:ios
   ```
   or use EAS Build:
   ```bash
   npx eas build --platform ios
   ```

### Android Build:
1. Generate a keystore (if not already done)
2. Build:
   ```bash
   npx expo build:android
   ```
   or use EAS Build:
   ```bash
   npx eas build --platform android
   ```

## 🔧 Additional Configuration Needed

### 1. Update Bundle Identifier / Package Name
- **iOS**: Change `com.velocity.app` in `app.json` to your unique bundle identifier
- **Android**: Change `com.velocity.app` in `app.json` to your unique package name (reverse domain format)

### 2. App Icons
- Ensure `./assets/images/icon.png` is 1024x1024px
- Ensure `./assets/images/adaptive-icon.png` is 1024x1024px (Android)

### 3. Permissions
- Location permissions are already configured
- Add other permissions as needed (camera, notifications, etc.)

### 4. Backend API Configuration
- Update the API endpoint in `app/index.tsx` (currently hardcoded to `http://192.168.0.135:8000`)
- Consider using environment variables for different environments

## 📝 Next Steps Checklist

- [ ] Install Xcode (iOS) or Android Studio (Android)
- [ ] Install CocoaPods (iOS only)
- [ ] Set up Android environment variables (Android only)
- [ ] Get Google Maps API keys for iOS and Android
- [ ] Add API keys to `app.json`
- [ ] Update bundle identifier/package name to your unique identifier
- [ ] Run `npm install` to ensure all dependencies are installed
- [ ] Test on iOS simulator/Android emulator
- [ ] Test on physical device
- [ ] Configure backend API endpoint

## 🐛 Troubleshooting

### iOS Issues:
- **"No bundle URL present"**: Run `npx expo start --clear`
- **Pod install fails**: Try `cd ios && pod deintegrate && pod install && cd ..`
- **Build errors**: Clean build folder in Xcode (Cmd+Shift+K)

### Android Issues:
- **"SDK location not found"**: Set ANDROID_HOME environment variable
- **"Command not found: adb"**: Add Android SDK platform-tools to PATH
- **Build fails**: Run `cd android && ./gradlew clean && cd ..`

## 📚 Resources

- [Expo Documentation](https://docs.expo.dev/)
- [React Native Maps Setup](https://github.com/react-native-maps/react-native-maps/blob/master/docs/installation.md)
- [Expo EAS Build](https://docs.expo.dev/build/introduction/)
