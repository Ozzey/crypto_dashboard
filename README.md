# Crypto Currency Dashboard Web Application

Welcome to the Crypto Currency Dashboard, a comprehensive web application designed for cryptocurrency enthusiasts and investors. This platform offers a rich set of features that allow users to track their portfolio, analyze market trends, and gain insights into the sentiments surrounding various cryptocurrencies. Utilizing the power of TradingView API for advanced charting and widgets, along with the Coingecko API for accurate and up-to-date OHLC (Open, High, Low, Close) data, our dashboard delivers a seamless and informative experience.

## Features

- **Live Cryptocurrency Data:** Access real-time price data, market capitalization, volume, and more for a wide range of cryptocurrencies.
- **Advanced Charting Tools:** Powered by TradingView API, our dashboard provides detailed and customizable graphs, allowing users to visualize market trends and perform technical analysis.
- **Portfolio Management:** Users can log in and manage their cryptocurrency portfolio, track their holdings, and see their portfolio's performance over time.
- **Sentiment Analysis:** Gain insights into the market sentiment of different coins. Analyze how the sentiments correlate with market movements and make informed decisions.
- **Responsive Design:** Whether you are on a desktop or a mobile device, our dashboard is fully responsive, ensuring a great user experience across all devices.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript (with frameworks/libraries as applicable)
- **Backend:** Python-Flask
- **Database:** SQLite - for storing user data and portfolio information securely.
- **APIs:**
  - **TradingView API:** For embedding advanced financial charts and widgets.
  - **Coingecko API:** For fetching real-time cryptocurrency data, including OHLC, volume, and market cap.

## Getting Started



---

## Docker Setup

To simplify the setup process and ensure a consistent environment across different machines, we've dockerized the Crypto Currency Dashboard application. Follow the steps below to build and run the Docker image.

### Prerequisites

Ensure you have Docker installed on your machine. If you haven't installed Docker yet, follow the instructions on the [official Docker documentation](https://docs.docker.com/get-docker/) to set it up for your operating system.

### Building the Docker Image

1. Open a terminal or command prompt.
2. Navigate to the root directory of the Crypto Currency Dashboard project.
3. Build the Docker image by running the following command:

```shell
docker build -t crypto_dashboard .
```

This command reads the `Dockerfile` in the project's root directory and builds a Docker image named `crypto_dashboard`.

### Running the Docker Container

Once the image has been built, you can run the application inside a Docker container using the following command:

```shell
docker run -p 5000:5000 crypto_dashboard
```

This command starts a container based on the `crypto_dashboard` image, mapping port 5000 of the container to port 5000 on your host machine.

### Accessing the Application

After the container starts, you can access the Crypto Currency Dashboard web application by navigating to `http://localhost:5000` in your web browser.

### Stopping the Container

To stop the running Docker container, you can press `Ctrl+C` in the terminal where the container is running. Alternatively, you can find the container ID using `docker ps` and then stop it using `docker stop <container_id>`.

---
