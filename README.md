## Table of Contents

* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
  * [Common](#common)
  * [Web and API Tests](#web-and-api-tests)
  * [Mobile Tests](#mobile-tests)
* [Test Execution](#test-execution)
* [CI/ CD](#ci-cd)
* [Framework Structure](#framework-structure)

## General Info

This project provides a comprehensive framework for automated testing of Web, Mobile, and API applications using Selenium, Appium, and Requests.

---

## Technologies

* **Programming Language:** Python 3.12
* **Build Tool:** pip
* **Test Automation Framework:** pytest
* **UI Testing:** Selenium WebDriver (custom implementation)
* **API Testing:** requests (custom implementation) + WireMock
* **Database:** MySQL + SQLAlchemy (JPA EntityManager)
* **Reporting:**
  * Allure
* **Parallel Execution:** 
  * Selenium Grid + pytest-xdist (Web) 
  * pytest-xdist (API & Mobile)
* **VCS:** GitHub
* **CI/CD:** Jenkins
* **Infrastructure:** Docker / Test Containers

---

## Setup

### Common

* Install Python 3.12.
* Activate environment
```bash
source .venv/bin/activate
```
* Install dependencies
```bash
pip install -r requirements.txt
```
* Build and start data bases via docker compose (if needed)
```bash
docker compose -f data/docker/docker-compose-mysql.yml up -d
```
* Build and start Selenium Grid via docker compose (if needed)
```bash
docker compose -f data/docker/docker-compose-selenium-grid.yml up -d
```
* Build and start Allure via docker compose (if needed)
```bash
docker compose -f data/docker/docker-compose-allure.yml up -d
```
  * Allure Reports:
    * Swagger: `http://localhost:5050/allure-docker-service/swagger/`
    * UI results: `http://localhost:5252/allure-docker-service-ui/projects/default`

### Web and API Tests
* MySQL DB, Selenium Grid, and WireMock are started automatically via Test Containers, if following configs are set
  *  payments_db_config.yaml -> db.infra: testcontainer
  *  products_db_config.yaml -> db.infra: testcontainer
  *  web_config.yaml -> selenium.grid: testcontainer
  *  api_config.yaml -> mock.service: testcontainer
* MySQL DB and Selenium Grid should be started via specific docker compose files, if following configs are set
  *  payments_db_config.yaml -> db.infra: dockercompose
  *  products_db_config.yaml -> db.infra: dockercompose
  *  web_config.yaml -> selenium.grid: dockercompose

* **BrowserStack Cloud Configuration** (`data/config/dev/web_config.yaml`):
```configs
driver.type=cloud
browser.name={BROWSER}
browser.version={VERSION}
cloud.os.name={OS}
cloud.os.version={OS_VERSION}
cloud.username={USERNAME}
cloud.accessKey={ACCESS_KEY}
cloud.session.name={SESSION_NAME}
cloud.build.name={BUILD_NAME}
```

### Mobile Tests

* **Local Devices / Simulators / Emulators**
  * **Android:** Install SDK, create and run virtual devices.
  * **iOS:** Install Xcode, create and run simulators.
* Appium server starts automatically in tests. No need to start it separately.
* **Debugging Locators Manually**
  * Install Appium Inspector
  * Start Appium server:
    ```bash
    appium --allow-insecure chromedriver_autodownload
    ```
  * Specify Appium Inspector capabilities and run, as example
  * **Sample Capabilities in Appium Inspector**
    * Android:
    ```json
    {
      "platformName": "Android",
      "appium:automationName": "UiAutomator2",
      "appium:udid": "emulator-5554",
      "appium:app": "/path/to/Android-SauceLabs.apk",
      "appium:avdLaunchTime": "180000"
    }
    ```
      * iOS:
    ```json
    {
      "platformName": "iOS",
      "appium:automationName": "XCUITest",
      "appium:deviceName": "iPhone 16e",
      "appium:app": "/path/to/Ios-SauceLabs.app",
      "appium:udid": "1CD043D1-CBD5-4088-8B60-7286829666C8"
    }
    ```
* **BrowserStack Cloud Configuration** (`data/config/dev/mobile_config.yaml`):
```configs
common.isCloud=true
cloud.credentials.username={USERNAME}
cloud.credentials.accessKey={ACCESS_KEY}

cloud.android.app={CLOUD_APP_LINK}
cloud.android.device.name={DEVICE}
cloud.android.device.platformVersion={VERSION}
cloud.android.sessionName={SESSION_NAME}
cloud.android.buildName={BUILD_NAME}

cloud.ios.app={CLOUD_APP_LINK}
cloud.ios.device.name={DEVICE}
cloud.ios.device.platformVersion={VERSION}
cloud.ios.sessionName={SESSION_NAME}
cloud.ios.buildName={BUILD_NAME}
```
* **Upload App to BrowserStack**
```bash
curl -u "{USERNAME}:{ACCESS_KEY}" \
  -X POST "https://api-cloud.browserstack.com/app-automate/upload" \
  -F "file=@/path/to/Android-SauceLabs.apk"
```
* Note: No signed iOS app available for BrowserStack farm.

---

## Test Execution

* Navigate to project directory.
* Run tests using Pytest:
```bash
# Execute Android/ iOS tests with in one thread
pytest -m android
pytest -m ios

# Execute Web tests with in one thread (concurrency level - classes).
# Data bases and Selenium Grid should be up before separately using specific docker compose file under /data/docker  
pytest -n 4 --dist=loadscope -m web --db_infra=dockercompose --selenium_grid=dockercompose --mock_service=local 

# Execute Web tests with in one thread.
# Data bases, Selenium Grid, WireMock will be up using test containers automatically.  
pytest -m web 
```

---

## CI/ CD
  * Start Jenkins locally
    ```bash
    brew services restart jenkins-lts
    ```
  * `http://localhost:8080/job/PythonWebTests/`
    * Run Python Web Tests in Jenkins Pipeline.
    * Tests run in a docker container. 
    * DB built and started in separate docker containers via docker compose. 
    * Selenium Grid built and started in a separate docker container via docker compose.
  * `http://localhost:8080/job/PythonApiTests/`
    * Run Python Api Tests in Jenkins Pipeline. 
    * Tests run in a docker container.
  * `http://localhost:8080/job/PythonAndroidTests/`
    * Python Android Tests.
    * All tests run on local environment.
  * `http://localhost:8080/job/PythonIosTests/`
    * Python iOS Tests. 
    * All tests run on local environment.

---

## **Framework Structure**

```
├── data                                  # Stores configurations, docker files, test data, mobile app files.
├── src.core
│   ├── api                               # Provides the core framework, service abstractions, and mock capabilities for API testing.
│   │   ├── core                          # Provides core classes for sending API requests, handling responses, and validating API responses in tests.
│   │   ├── mock                          # Provides higher-level mock API functionality.
│   │   └── service                       # Provides high-level service managers for interacting with various API domains.
│   ├── data                              # Provides test data structures, factories, and enumerations for API, web, and mobile testing.
│   │   ├── configs                       # Provides classes and interfaces for loading and managing application configs for different environments, including API, database, web, and mobile.
│   │   └── factory                       # Provides generic factories and data builders for creating or retrieving test data.
│   ├── db                                # Provides core database management and EntityManager support.
│   │   ├── client                        # Provides database client implementations for interacting with different database domains.
│   │   └── core                          # Provides utilities and abstractions for managing DB entities.
│   │   └── infra                         # Provides infrastructure for running MySQL-based test database services.
│   ├── mobile                            # Contains core classes and abstractions for mobile testing.
│   │   ├── appiumservice/                # Provides Appium service management for mobile test automation.
│   │   ├── assertions/                   # Provides assertion utilities for validating mobile applications under test.
│   │   ├── data/                         # Provides data structures and test data sources for mobile application testing.
│   │   ├── driver/                       # Provides driver implementations and factories for mobile testing using Appium.
│   │   ├── manager/                      # Provides classes for managing mobile devices, apps, and drivers in Appium tests.
│   │   ├── model/                        # Provides core data models used across mobile testing and automation frameworks.
│   │   ├── pageobject/                   # Contains Page Object classes for mobile testing across Android and iOS platforms.
│   │   └── util/                         # Provides utility classes and helpers for mobile test automation.
│   ├── util                              # Utility classes and helpers for the automation framework.
│   │   ├── platformshared/               # Provides shared utilities, abstractions, and helpers for platform-independent test automation.
│   │   └── system/                       # Utilities for system-level operations in the automation framework.
│   └── web                               # This package contains classes related to the web testing layer.
│       ├── assertions/                   # Provides assertion classes for validating the state and behavior of web pages in tests.
│       ├── data/                         # Provides data-related utilities and resources for web testing.
│       ├── driver/                       # Provides WebDriver implementations and factories for initializing web browsers in tests.
│       ├── infra                         # Provides infrastructure for running Selenium Grid.
│       ├── manager/                      # Provides classes for managing the lifecycle and state of the web application under test.
│       └── pageobject/                   # Provides page object classes for web application pages.
├── src.tests
│   ├── api                               # API tests.
│   ├── mobile                            # Mobile tests.
│   └── web                               # Web tests
```
