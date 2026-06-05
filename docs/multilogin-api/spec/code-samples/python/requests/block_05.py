{
    "browser_type": "<string>",
    "os_type": "<string>",
    "script_file": "<string>",
    "automation": "<string>",
    "core_version": <integer>,
    "core_minor_version": <integer>,
    "is_headless": <boolean>,
    "parameters": {
        "flags": {
            "audio_masking": "<string>",
            "fonts_masking": "<string>",
            "geolocation_masking": "<string>",
            "geolocation_popup": "<string>",
            "graphics_masking": "<string>",
            "graphics_noise": "<string>",
            "localization_masking": "<string>",
            "media_devices_masking": "<string>",
            "navigator_masking": "<string>",
            "ports_masking": "<string>",
            "proxy_masking": "<string>",
            "screen_masking": "<string>",
            "timezone_masking": "<string>",
            "webrtc_masking": "<string>",
            "canvas_noise:": "<string>",
            "startup_behavior": "<string>"
        },
        "proxy": {
            "host": "<string>",
            "type": "<string>",
            "port": <integer>,
            "username": "<string>",
            "password": "<string>"
        },
        "fingerprint": {
            "navigator": {
                "hardware_concurrency": <integer>,
                "platform": "<string>",
                "user_agent": "<string>",
                "os_cpu": "<string>"
            },
            "localization": {
                "languages": "<string>",
                "locale": "<string>",
                "accept_languages": "<string>"
            },
            "timezone": {
                "zone": "<string>"
            },
            "graphic": {
                "renderer": "<string>",
                "vendor": "<string>"
            },
            "webrtc": {
                "public_ip": "<string>"
            },
            "media_devices": {
                "audio_inputs": <integer>,
                "audio_outputs": <integer>,
                "video_inputs": <integer>
            },
            "screen": {
                "height": <integer>,
                "pixel_ratio": <double>,
                "width": <integer>
            },
            "geolocation": {
                "accuracy": <number>,
                "altitude": <number>,
                "latitude": <number>,
                "longitude": <number>
            },
            "ports": [
                <integer>,
            ],
            "fonts": [
                "<string>"
            ],
            "cmd_params": {
                "params": [
                    {
                        "flag": "<string>",
                        "value": "<boolean>"
                    }
                ]
            }
        },
        "custom_start_urls": [
            "<string>"
        ]
    }
}
