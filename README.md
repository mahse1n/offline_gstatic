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

------------------------------------------------------------------------

# Initial Setup (Caching Resources)

Before using the server in an offline or blackout scenario:

1.  Start the server **while internet access is available**
2.  Run your application normally
3.  Use the application for a while

During this time the server will **automatically cache required
resources**.

After enough resources are cached, the application will be able to
**continue functioning without internet access**.

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
potentially benefit from a **local caching proxy**.

------------------------------------------------------------------------

# Recommended Workflow

1.  Start the proxy server
2.  Ensure internet access is available
3.  Run your application normally
4.  Allow the server to cache required assets
5.  Once cached, the application can continue working during network
    disruptions

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
