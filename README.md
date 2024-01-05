# Subdomain Enumeration Script

A Python script for subdomain enumeration using various online tools and `httpx`.

## Overview

This script helps in collecting subdomains for a given target by leveraging online services like crt.sh, rapiddns.io, and jldc.me. It then uses `httpx` to check the availability of these subdomains.

## Prerequisites

- Python 3.x
- Go (latest version)
- `httpx` toolkit

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sanskaros/enumerator.git
    ```

2. **Navigate to the script directory:**

    ```bash
    cd enumerator
    ```

3. **Run the script:**

    ```bash
    python3 enumerator.py
    ```

4. **Follow the on-screen instructions to provide the target URL.**

## Output

- The script generates a file named `<target>.txt` containing the results.

## Notes

- Ensure you have the latest version of Go.
  Here's how:

  - Go to the official Go download page: [https://golang.org/dl/](https://golang.org/dl/)
  - Find the version you want to install, right-click on the "Download" link, and copy the link address.
  - Download and extract it using these commands:

    ```bash
    wget https://golang.org/dl/go1.17.linux-amd64.tar.gz
    sudo tar -C /usr/local -xzf go1.17.linux-amd64.tar.gz
    ```

  - Set environment variables:

    ```bash
    echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
    echo 'export GOPATH=$HOME/go' >> ~/.bashrc
    ```

    If on WSL, refresh your profile:

    ```bash
    source ~/.bashrc
    ```

    Or restart your Linux or Windows.

  - Remove previous versions of Go.

- Ensure you have the `httpx` toolkit installed. You can install it using:

    ```bash
    pip install httpx
    ```

    Or clone from this repository:

    ```bash
    git clone https://github.com/projectdiscovery/httpx.git
    ```

    And make sure to do this in the `go/bin` folder.

## Author

- Stat_of_mind

## Version

- 0.0.1
- 1.0.0 (latest)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
