# IP Info Tool

A simple Python script to fetch IP address information using [ip-api.com](http://ip-api.com). The output is displayed in a readable format using the `rich` library.

---

## Features

- Fetch information about your own IP or any target IP.
- Displays data in a clean JSON format.
- Lightweight and easy to use.

---

## Requirements

- Python 3
- `requests` library
- `rich` library

You can install the required libraries using:

```bash
pip install requests rich
````

---

## Usage

```bash
python ip_info.py [IP_ADDRESS]
```

* `[IP_ADDRESS]` is optional.

  * If provided, the script fetches information for that IP.
  * If omitted, it fetches information about your own IP.

**Examples:**

```bash
# Get information about your own IP
python ip_info.py

# Get information about a target IP
python ip_info.py 8.8.8.8
```

---

## Output

The script returns a JSON object with details such as:

* `status` – success or fail
* `country`
* `regionName`
* `city`
* `zip`
* `lat` / `lon` – latitude and longitude
* `isp` – Internet Service Provider
* `query` – the IP address queried

Example:

```json
{
    "status": "success",
    "country": "United States",
    "regionName": "California",
    "city": "Mountain View",
    "zip": "94035",
    "lat": 37.386,
    "lon": -122.0838,
    "isp": "Google LLC",
    "query": "8.8.8.8"
}
```

---

## Installation

Clone the repository or download the script:

```bash
git clone https://github.com/yourusername/ip-info-tool.git
cd ip-info-tool
```

Make the script executable (optional):

```bash
chmod +x ip_info.py
./ip_info.py
```

---

## License

This project is licensed under the MIT License.

[![Watch the video](https://img.youtube.com/vi/wJqK2K7oNoE/hqdefault.jpg)](https://www.youtube.com/watch?v=wJqK2K7oNoE)


```
