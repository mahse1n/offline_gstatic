# Local GStatic Cache Proxy

Local GStatic Cache Proxy is a small local server designed to **cache
and mirror resources normally served from gstatic**.\
It allows applications---especially **Flutter web applications**---to
continue functioning during **internet outages, censorship, or network
blackouts** by serving previously cached static resources from a local
machine.

The server runs on **localhost** and works as a **fallback cache**: - If
a requested file exists in the cache → it is served locally. - If the
file is missing → the server fetches it from the real source (when
internet access is available) and stores it for future use.

This design allows developers to **preload and cache critical resources
before a blackout happens**.

------------------------------------------------------------------------

# Initial Setup (Caching Resources)

Before using the server in an offline or blackout scenario:

## If you have good internet access right now

1.  Start the server **while internet access is available**
2.  Run your application normally
3.  Use the application for a while


During this time the server will **automatically cache required
resources**.

After enough resources are cached, the application will be able to
**continue functioning without internet access**.

## If your internet connection is poor right now
1. You can **use a snapshot branch on this report**
2. run your application, if there be no cache misses, everything will be good

------------------------------------------------------------------------

# Do before using
this server runs on the localhost and for applicaiton to request this server instead of the real gstatic, you have to change the DNS settings,

## windows
1. use **WIN + R** to open run widnows, write **notepad** and use **cntrl + shift + enter** for administrator privileges.
2. open the file hosts in the path `C:\Windows\System32\drivers\etc\hosts`
3. add these lines in the files and save:
```
# Added by offline_gstatic
127.0.0.1  www.gstatic.com
127.0.0.1  gstatic.com
127.0.0.1  fonts.gstatic.com
# End of section
```
## linux
1. with **sudo** access, use an editor to edit the hosts file located at `/etc/hosts`
2. add these lines and save:
```
# Added by offline_gstatic
127.0.0.1  www.gstatic.com
127.0.0.1  gstatic.com
127.0.0.1  fonts.gstatic.com
# End of section
```
------------------------------------------------------------------------

# Usage with Flutter

This project was designed specifically with **Flutter Web** in mind.

When running a Flutter web project, use the following flags:

    flutter run \
    --no-pub \
    --no-web-resources-cdn \
    --web-browser-flag="--ignore-certificate-errors"

Explanation:

-   `--no-pub`\
    Prevents dependency fetching during runtime.

-   `--no-web-resources-cdn`\
    Stops Flutter from using external CDN resources.

-   `--web-browser-flag="--ignore-certificate-errors"`\
    Allows the browser to ignore certificate warnings when using the
    local proxy.

These flags help ensure Flutter loads resources through the **local
caching server instead of remote CDNs**.

------------------------------------------------------------------------

# Using With Other Projects

Although built for Flutter, this server can also be used with:

-   web applications
-   development environments
-   local CDN fallback testing
-   offline development environments

Any project that normally loads resources from external CDNs can
potentially benefit from a **local caching proxy**. other frameworks may have setting to disable live static loadings, flutter doesnt allow it for the gstatic files; It is better to try that way first.

------------------------------------------------------------------------

# Recommended Workflow

1.  Start the proxy server
2.  Ensure internet access is available
3.  Run your application normally
4.  Allow the server to cache required assets
5.  Once cached, the application can continue working during network
    disruptions

------------------------------------------------------------------------

# What to do if the certs expired
If the certificates used by the local server expire, browsers may refuse to connect to the server or show security warnings. This happens because HTTPS certificates have a limited validity period.

When the certificates expire, you need to generate new ones and replace the old files used by the server.

1. First stop the local server.
2. Delete or move the old certificate files from the project directory.
3. Then generate new self-signed certificates using OpenSSL. Run the following command in the project directory:
```
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 3650 -nodes
```
This command generates a new private key and certificate that will be valid for about ten years.


Make sure the generated certificate and key filenames match the filenames expected by the server. If the project already uses specific filenames, replace the old files with the newly generated ones.

After generating the new certificates, start the server again.

Some browsers may still show warnings because the certificate is self-signed. If you are using Flutter for development, you can run the browser with the ignore certificate errors flag as described in the main documentation.

If problems continue after replacing the certificates, clear the browser cache or restart the browser so it reloads the new certificate.

------------------------------------------------------------------------

# Features

-   Local caching proxy for static resources
-   Designed with **Flutter Web** compatibility in mind
-   Works on **localhost**
-   Automatically caches missing resources when internet access is
    available
-   Allows applications to continue running when external CDNs become
    unreachable
-   Can also be used for **other web projects**, not just Flutter

------------------------------------------------------------------------

# Educational Purpose & Disclaimer

This project is provided **strictly for educational purposes, research,
and resilience against internet blackouts**.

It is intended to help developers understand:

-   offline infrastructure
-   CDN fallback mechanisms
-   caching proxies
-   resilience during network outages

------------------------------------------------------------------------

# How It Works

1.  The local server acts as a **proxy/cache** for static resources.
2.  When a resource is requested:
    -   If it exists in the **local cache**, it is served immediately.
    -   If it does **not exist**, the server requests the resource from
        the real internet source.
3.  The downloaded resource is then **stored locally** for future
    requests.

Once cached, the resource can be served **even if the internet is
unavailable**.

⚠️ **Important Notice**

The author of this project **is not responsible for any misuse of this
software**.

If someone attempts to use this tool for: - bypassing services -
violating terms of service - malicious activity - or any other misuse

that responsibility lies **entirely with the user**.

By using this project you agree that:

-   You understand the purpose is **educational and resilience testing**
-   You will **not use it in ways that violate laws or platform
    policies**
-   The author **takes no responsibility for misuse**

------------------------------------------------------------------------

# Contributing

Contributions are welcome. Improvements may include:

-   smarter caching logic
-   additional CDN support
-   cache management tools
-   logging and diagnostics

------------------------------------------------------------------------

# License

This project is provided for **educational and research purposes**.

Use responsibly.
