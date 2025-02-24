{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TiruveedulaAjay/Bank-chatbot/blob/main/banking.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 48,
      "metadata": {
        "id": "nW9aK4g7Fvyh"
      },
      "outputs": [],
      "source": [
        "import streamlit as str\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"/BankFAQs.csv\")"
      ],
      "metadata": {
        "id": "34VfRkf8NnpQ"
      },
      "execution_count": None,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "Mxk3HazZHRvl",
        "outputId": "e5a20410-d1f5-4fb2-8207-824361f831da"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                            Question  \\\n",
              "0  Do I need to enter ‘#’ after keying in my Card...   \n",
              "1  What details are required when I want to perfo...   \n",
              "2  How should I get the IVR Password  if I hold a...   \n",
              "3  How do I register my Mobile number for IVR Pas...   \n",
              "4                  How can I obtain an IVR Password    \n",
              "\n",
              "                                              Answer     Class  \n",
              "0  Please listen to the recorded message and foll...  security  \n",
              "1  To perform a secure IVR transaction, you will ...  security  \n",
              "2  An IVR password can be requested only from the...  security  \n",
              "3  Please call our Customer Service Centre and en...  security  \n",
              "4  By Sending SMS request: Send an SMS 'PWD<space...  security  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-57c7e777-71d2-4e29-b48e-ff5c751d9c2b\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Question</th>\n",
              "      <th>Answer</th>\n",
              "      <th>Class</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Do I need to enter ‘#’ after keying in my Card...</td>\n",
              "      <td>Please listen to the recorded message and foll...</td>\n",
              "      <td>security</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>What details are required when I want to perfo...</td>\n",
              "      <td>To perform a secure IVR transaction, you will ...</td>\n",
              "      <td>security</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>How should I get the IVR Password  if I hold a...</td>\n",
              "      <td>An IVR password can be requested only from the...</td>\n",
              "      <td>security</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>How do I register my Mobile number for IVR Pas...</td>\n",
              "      <td>Please call our Customer Service Centre and en...</td>\n",
              "      <td>security</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>How can I obtain an IVR Password</td>\n",
              "      <td>By Sending SMS request: Send an SMS 'PWD&lt;space...</td>\n",
              "      <td>security</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-57c7e777-71d2-4e29-b48e-ff5c751d9c2b')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:None;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: None;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: None;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-57c7e777-71d2-4e29-b48e-ff5c751d9c2b button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'None';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-57c7e777-71d2-4e29-b48e-ff5c751d9c2b');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-6c475b96-9061-4273-878b-ee7548f215f3\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-6c475b96-9061-4273-878b-ee7548f215f3')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:None;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: None;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: None;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: None;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = True;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-6c475b96-9061-4273-878b-ee7548f215f3 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'None';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 1764,\n  \"fields\": [\n    {\n      \"column\": \"Question\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 1334,\n        \"samples\": [\n          \"What if I have already obtained a MIN\",\n          \"Are there transaction limits for Debit Card\",\n          \"What is the HDFC Bank Contactless MulticurrencyForexPlus card\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Answer\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 1440,\n        \"samples\": [\n          \"You can take a Education Loan for foreign education on the following courses: Management Courses (Full-Time) Engineering Courses Medicine - Graduation + Post Graduation Masters in Computer Application ( MCA / MCM ) Architecture Hotel and Hospitality Agriculture Pure Science View more\",\n          \"Your insurance cover starts from the commencement date indicated by you in the proposal form or receipt of the premium by us, whichever is later.\",\n          \"The policy provides a family discount of 10%, if 3 or more family members are covered under a single policy on an individual sum insured basis.\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Class\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"security\",\n          \"loans\",\n          \"fundstransfer\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 7
        }
      ],
      "source": [
        "df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kJ7zjApjHXOY",
        "outputId": "12c58ee6-6ca8-4f9b-ae1e-ce6e458eeb5e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1764 entries, 0 to 1763\n",
            "Data columns (total 3 columns):\n",
            " #   Column    Non-None Count  Dtype \n",
            "---  ------    --------------  ----- \n",
            " 0   Question  1764 non-None   object\n",
            " 1   Answer    1764 non-None   object\n",
            " 2   Class     1764 non-None   object\n",
            "dtypes: object(3)\n",
            "memory usage: 41.5+ KB\n"
          ]
        }
      ],
      "source": [
        "df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "id": "4XaVTOtgHcbe",
        "outputId": "537d906d-e191-474c-93ab-fd6bf9d4e38e"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         count unique                                                top freq\n",
              "Question  1764   1334  How can I change the mode of repayment/ accoun...   18\n",
              "Answer    1764   1440  Post Dated Cheques(PDCs)/Security Cheques subm...   17\n",
              "Class     1764      7                                          insurance  469"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-f53bf7e8-a295-47b1-acce-9b6eddb777de\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "      <th>unique</th>\n",
              "      <th>top</th>\n",
              "      <th>freq</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Question</th>\n",
              "      <td>1764</td>\n",
              "      <td>1334</td>\n",
              "      <td>How can I change the mode of repayment/ accoun...</td>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Answer</th>\n",
              "      <td>1764</td>\n",
              "      <td>1440</td>\n",
              "      <td>Post Dated Cheques(PDCs)/Security Cheques subm...</td>\n",
              "      <td>17</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Class</th>\n",
              "      <td>1764</td>\n",
              "      <td>7</td>\n",
              "      <td>insurance</td>\n",
              "      <td>469</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-f53bf7e8-a295-47b1-acce-9b6eddb777de')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:None;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: None;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: None;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-f53bf7e8-a295-47b1-acce-9b6eddb777de button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'None';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-f53bf7e8-a295-47b1-acce-9b6eddb777de');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-53fe52cc-59a0-43de-a445-0d4d188981c7\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-53fe52cc-59a0-43de-a445-0d4d188981c7')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:None;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: None;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: None;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: None;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = True;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-53fe52cc-59a0-43de-a445-0d4d188981c7 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'None';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 3,\n  \"fields\": [\n    {\n      \"column\": \"count\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": \"1764\",\n        \"max\": \"1764\",\n        \"num_unique_values\": 1,\n        \"samples\": [\n          \"1764\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"unique\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": 7,\n        \"max\": 1440,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          1334\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"top\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"How can I change the mode of repayment/ account for my loan\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"freq\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": \"17\",\n        \"max\": \"469\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"18\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 9
        }
      ],
      "source": [
        "df.describe().T"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 335
        },
        "id": "-2qJMFTTHk32",
        "outputId": "dca96993-b08f-43e2-e013-b551f761d018"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Class\n",
              "insurance        469\n",
              "cards            403\n",
              "loans            375\n",
              "accounts         306\n",
              "investments      140\n",
              "security          57\n",
              "fundstransfer     14\n",
              "Name: count, dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Class</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>insurance</th>\n",
              "      <td>469</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>cards</th>\n",
              "      <td>403</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>loans</th>\n",
              "      <td>375</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>accounts</th>\n",
              "      <td>306</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>investments</th>\n",
              "      <td>140</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>security</th>\n",
              "      <td>57</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>fundstransfer</th>\n",
              "      <td>14</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ],
      "source": [
        "df['Class'].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "id": "IvyGJB3iHvka"
      },
      "outputs": [],
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer\n",
        "vectorizer = CountVectorizer()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "id": "arCAJwWAIKbu"
      },
      "outputs": [],
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AYRWtBAgIzRN",
        "outputId": "97581c9b-9b93-4755-9926-b72d92aab0b8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1411, 3)\n"
          ]
        }
      ],
      "source": [
        "train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)\n",
        "print(train_data.shape)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hesXnCG9KKMY",
        "outputId": "a33823b6-5752-4700-a54a-89ea2aa9a1e8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1107           Can I reinstate the policy if it is lapsed\n",
            "212     Which course related expense does this loan co...\n",
            "1725        Where I can earn ‘Thanks Again’ Reward Points\n",
            "1518    I'm not a traveller, can I still benefit from ...\n",
            "1296    Is priority in allotment given to applications...\n",
            "                              ...                        \n",
            "265                                           What is PDC\n",
            "611          What if certain RD installments are not paid\n",
            "1100    What are the different plan options available ...\n",
            "1280       How do I know my application has been accepted\n",
            "598     Can I have a Super saver facility and a Sweep-...\n",
            "Name: Question, Length: 353, dtype: object\n"
          ]
        }
      ],
      "source": [
        "# Transform the text data into feature vectors\n",
        "X_train = vectorizer.fit_transform(train_data['Question'])\n",
        "X_test = vectorizer.transform(test_data['Question'])\n",
        "print(test_data['Question'])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w8Q9HlhOMJ0a",
        "outputId": "d357bddf-c3a0-4654-a9dc-e68374f15769"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1107      insurance\n",
            "212           loans\n",
            "1725          cards\n",
            "1518          cards\n",
            "1296    investments\n",
            "           ...     \n",
            "265           loans\n",
            "611        accounts\n",
            "1100      insurance\n",
            "1280    investments\n",
            "598        accounts\n",
            "Name: Class, Length: 353, dtype: object\n"
          ]
        }
      ],
      "source": [
        "#define the labels\n",
        "y_train = train_data['Class']\n",
        "y_test = test_data['Class']\n",
        "print(test_data['Class'])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "id": "21dd3Ec_M3cN"
      },
      "outputs": [],
      "source": [
        "from sklearn.svm import SVC"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 80
        },
        "id": "LbfCzLgWM-Vx",
        "outputId": "3b074346-63cb-4029-d070-0e7907d37ed0"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "SVC(C=1, gamma=0.01)"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {\n",
              "  /* Definition of color scheme common for light and dark mode */\n",
              "  --sklearn-color-text: #000;\n",
              "  --sklearn-color-text-muted: #666;\n",
              "  --sklearn-color-line: gray;\n",
              "  /* Definition of color scheme for unfitted estimators */\n",
              "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
              "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
              "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
              "  --sklearn-color-unfitted-level-3: chocolate;\n",
              "  /* Definition of color scheme for fitted estimators */\n",
              "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
              "  --sklearn-color-fitted-level-1: #d4ebff;\n",
              "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
              "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
              "\n",
              "  /* Specific color for light theme */\n",
              "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
              "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-icon: #696969;\n",
              "\n",
              "  @media (prefers-color-scheme: dark) {\n",
              "    /* Redefinition of color scheme for dark theme */\n",
              "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
              "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-icon: #878787;\n",
              "  }\n",
              "}\n",
              "\n",
              "#sk-container-id-1 {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 pre {\n",
              "  padding: 0;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-hidden--visually {\n",
              "  border: 0;\n",
              "  clip: rect(1px 1px 1px 1px);\n",
              "  clip: rect(1px, 1px, 1px, 1px);\n",
              "  height: 1px;\n",
              "  margin: -1px;\n",
              "  overflow: hidden;\n",
              "  padding: 0;\n",
              "  position: absolute;\n",
              "  width: 1px;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-dashed-wrapped {\n",
              "  border: 1px dashed var(--sklearn-color-line);\n",
              "  margin: 0 0.4em 0.5em 0.4em;\n",
              "  box-sizing: border-box;\n",
              "  padding-bottom: 0.4em;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-container {\n",
              "  /* jupyter's `normalize.less` sets `[hidden] { display: None; }`\n",
              "     but bootstrap.min.css set `[hidden] { display: None !important; }`\n",
              "     so we also need the `!important` here to be able to override the\n",
              "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
              "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
              "  display: inline-block !important;\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-text-repr-fallback {\n",
              "  display: None;\n",
              "}\n",
              "\n",
              "div.sk-parallel-item,\n",
              "div.sk-serial,\n",
              "div.sk-item {\n",
              "  /* draw centered vertical line to link estimators */\n",
              "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
              "  background-size: 2px 100%;\n",
              "  background-repeat: no-repeat;\n",
              "  background-position: center center;\n",
              "}\n",
              "\n",
              "/* Parallel-specific style estimator block */\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item::after {\n",
              "  content: \"\";\n",
              "  width: 100%;\n",
              "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
              "  flex-grow: 1;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel {\n",
              "  display: flex;\n",
              "  align-items: stretch;\n",
              "  justify-content: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:first-child::after {\n",
              "  align-self: flex-end;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:last-child::after {\n",
              "  align-self: flex-start;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:only-child::after {\n",
              "  width: 0;\n",
              "}\n",
              "\n",
              "/* Serial-specific style estimator block */\n",
              "\n",
              "#sk-container-id-1 div.sk-serial {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "  align-items: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  padding-right: 1em;\n",
              "  padding-left: 1em;\n",
              "}\n",
              "\n",
              "\n",
              "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
              "clickable and can be expanded/collapsed.\n",
              "- Pipeline and ColumnTransformer use this feature and define the default style\n",
              "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
              "*/\n",
              "\n",
              "/* Pipeline and ColumnTransformer style (default) */\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable {\n",
              "  /* Default theme specific background. It is overwritten whether we have a\n",
              "  specific estimator or a Pipeline/ColumnTransformer */\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "/* Toggleable label */\n",
              "#sk-container-id-1 label.sk-toggleable__label {\n",
              "  cursor: pointer;\n",
              "  display: flex;\n",
              "  width: 100%;\n",
              "  margin-bottom: 0;\n",
              "  padding: 0.5em;\n",
              "  box-sizing: border-box;\n",
              "  text-align: center;\n",
              "  align-items: start;\n",
              "  justify-content: space-between;\n",
              "  gap: 0.5em;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label .caption {\n",
              "  font-size: 0.6rem;\n",
              "  font-weight: lighter;\n",
              "  color: var(--sklearn-color-text-muted);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label-arrow:before {\n",
              "  /* Arrow on the left of the label */\n",
              "  content: \"▸\";\n",
              "  float: left;\n",
              "  margin-right: 0.25em;\n",
              "  color: var(--sklearn-color-icon);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "/* Toggleable content - dropdown */\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content {\n",
              "  max-height: 0;\n",
              "  max-width: 0;\n",
              "  overflow: hidden;\n",
              "  text-align: left;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content pre {\n",
              "  margin: 0.2em;\n",
              "  border-radius: 0.25em;\n",
              "  color: var(--sklearn-color-text);\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content.fitted pre {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
              "  /* Expand drop-down */\n",
              "  max-height: 200px;\n",
              "  max-width: 100%;\n",
              "  overflow: auto;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
              "  content: \"▾\";\n",
              "}\n",
              "\n",
              "/* Pipeline/ColumnTransformer-specific style */\n",
              "\n",
              "#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator-specific style */\n",
              "\n",
              "/* Colorize estimator box */\n",
              "#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label label.sk-toggleable__label,\n",
              "#sk-container-id-1 div.sk-label label {\n",
              "  /* The background is the default theme color */\n",
              "  color: var(--sklearn-color-text-on-default-background);\n",
              "}\n",
              "\n",
              "/* On hover, darken the color of the background */\n",
              "#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "/* Label box, darken color on hover, fitted */\n",
              "#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator label */\n",
              "\n",
              "#sk-container-id-1 div.sk-label label {\n",
              "  font-family: monospace;\n",
              "  font-weight: bold;\n",
              "  display: inline-block;\n",
              "  line-height: 1.2em;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label-container {\n",
              "  text-align: center;\n",
              "}\n",
              "\n",
              "/* Estimator-specific */\n",
              "#sk-container-id-1 div.sk-estimator {\n",
              "  font-family: monospace;\n",
              "  border: 1px dotted var(--sklearn-color-border-box);\n",
              "  border-radius: 0.25em;\n",
              "  box-sizing: border-box;\n",
              "  margin-bottom: 0.5em;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "/* on hover */\n",
              "#sk-container-id-1 div.sk-estimator:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
              "\n",
              "/* Common style for \"i\" and \"?\" */\n",
              "\n",
              ".sk-estimator-doc-link,\n",
              "a:link.sk-estimator-doc-link,\n",
              "a:visited.sk-estimator-doc-link {\n",
              "  float: right;\n",
              "  font-size: smaller;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1em;\n",
              "  height: 1em;\n",
              "  width: 1em;\n",
              "  text-decoration: None !important;\n",
              "  margin-left: 0.5em;\n",
              "  text-align: center;\n",
              "  /* unfitted */\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted,\n",
              "a:link.sk-estimator-doc-link.fitted,\n",
              "a:visited.sk-estimator-doc-link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: None;\n",
              "}\n",
              "\n",
              "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: None;\n",
              "}\n",
              "\n",
              "/* Span, style for the box shown on hovering the info icon */\n",
              ".sk-estimator-doc-link span {\n",
              "  display: None;\n",
              "  z-index: 9999;\n",
              "  position: relative;\n",
              "  font-weight: normal;\n",
              "  right: .2ex;\n",
              "  padding: .5ex;\n",
              "  margin: .5ex;\n",
              "  width: min-content;\n",
              "  min-width: 20ex;\n",
              "  max-width: 50ex;\n",
              "  color: var(--sklearn-color-text);\n",
              "  box-shadow: 2pt 2pt 4pt #999;\n",
              "  /* unfitted */\n",
              "  background: var(--sklearn-color-unfitted-level-0);\n",
              "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted span {\n",
              "  /* fitted */\n",
              "  background: var(--sklearn-color-fitted-level-0);\n",
              "  border: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link:hover span {\n",
              "  display: block;\n",
              "}\n",
              "\n",
              "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link {\n",
              "  float: right;\n",
              "  font-size: 1rem;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1rem;\n",
              "  height: 1rem;\n",
              "  width: 1rem;\n",
              "  text-decoration: None;\n",
              "  /* unfitted */\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "#sk-container-id-1 a.estimator_doc_link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: None;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>SVC(C=1, gamma=0.01)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow\"><div><div>SVC</div></div><div><a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.6/modules/generated/sklearn.svm.SVC.html\">?<span>Documentation for SVC</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></div></label><div class=\"sk-toggleable__content fitted\"><pre>SVC(C=1, gamma=0.01)</pre></div> </div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ],
      "source": [
        "# train the SVM model\n",
        "svm_model = SVC(C=1, kernel='rbf', gamma=0.01, decision_function_shape='ovr')\n",
        "svm_model.fit(X_train, y_train)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ey6ZWRJZOHHi",
        "outputId": "e615a703-1021-491c-da71-569acd03e635"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  (0, 164)\t1\n",
            "  (0, 522)\t1\n",
            "  (0, 574)\t1\n",
            "  (0, 580)\t1\n",
            "  (0, 829)\t1\n",
            "  (0, 1084)\t1\n",
            "  (1, 253)\t1\n",
            "  (1, 255)\t1\n",
            "  (1, 337)\t1\n",
            "  (1, 364)\t2\n",
            "  (1, 408)\t1\n",
            "  (1, 445)\t1\n",
            "  (1, 447)\t1\n",
            "  (1, 624)\t1\n",
            "  (1, 625)\t1\n",
            "  (1, 914)\t1\n",
            "  (1, 1092)\t1\n",
            "  (1, 1194)\t1\n",
            "  (2, 42)\t1\n",
            "  (2, 164)\t1\n",
            "  (2, 354)\t1\n",
            "  (2, 827)\t1\n",
            "  (2, 950)\t1\n",
            "  (2, 1192)\t1\n",
            "  (3, 121)\t1\n",
            "  :\t:\n",
            "  (350, 1084)\t1\n",
            "  (350, 1092)\t1\n",
            "  (350, 1134)\t1\n",
            "  (350, 1189)\t1\n",
            "  (351, 16)\t1\n",
            "  (351, 71)\t1\n",
            "  (351, 117)\t1\n",
            "  (351, 332)\t1\n",
            "  (351, 495)\t1\n",
            "  (351, 516)\t1\n",
            "  (351, 597)\t1\n",
            "  (351, 709)\t1\n",
            "  (352, 21)\t1\n",
            "  (352, 59)\t1\n",
            "  (352, 164)\t1\n",
            "  (352, 415)\t2\n",
            "  (352, 496)\t1\n",
            "  (352, 528)\t1\n",
            "  (352, 750)\t1\n",
            "  (352, 966)\t1\n",
            "  (352, 970)\t1\n",
            "  (352, 972)\t1\n",
            "  (352, 1053)\t1\n",
            "  (352, 1059)\t1\n",
            "  (352, 1084)\t1\n"
          ]
        }
      ],
      "source": [
        "# made predictions on the test set\n",
        "svm_predictions = svm_model.predict(X_test)\n",
        "print(X_test)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zr1kr4SfOhSx",
        "outputId": "1fbecbc1-a50a-424d-cf32-29d2bcf97ca0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['insurance' 'loans' 'insurance' 'cards' 'insurance' 'insurance'\n",
            " 'insurance' 'accounts' 'insurance' 'accounts' 'cards' 'insurance'\n",
            " 'insurance' 'insurance' 'accounts' 'insurance' 'accounts' 'cards' 'loans'\n",
            " 'loans' 'insurance' 'loans' 'insurance' 'insurance' 'insurance'\n",
            " 'accounts' 'loans' 'insurance' 'cards' 'cards' 'insurance' 'cards'\n",
            " 'accounts' 'insurance' 'loans' 'loans' 'insurance' 'security' 'insurance'\n",
            " 'loans' 'insurance' 'loans' 'cards' 'insurance' 'insurance' 'loans'\n",
            " 'cards' 'insurance' 'cards' 'loans' 'cards' 'accounts' 'accounts'\n",
            " 'insurance' 'investments' 'cards' 'insurance' 'loans' 'cards' 'insurance'\n",
            " 'investments' 'insurance' 'insurance' 'accounts' 'cards' 'accounts'\n",
            " 'insurance' 'insurance' 'insurance' 'cards' 'insurance' 'insurance'\n",
            " 'cards' 'loans' 'insurance' 'insurance' 'loans' 'insurance' 'insurance'\n",
            " 'cards' 'insurance' 'insurance' 'accounts' 'accounts' 'insurance'\n",
            " 'insurance' 'accounts' 'insurance' 'insurance' 'accounts' 'loans' 'cards'\n",
            " 'insurance' 'insurance' 'loans' 'accounts' 'cards' 'insurance' 'loans'\n",
            " 'accounts' 'loans' 'insurance' 'accounts' 'loans' 'cards' 'accounts'\n",
            " 'cards' 'insurance' 'cards' 'insurance' 'insurance' 'accounts' 'accounts'\n",
            " 'loans' 'insurance' 'insurance' 'insurance' 'accounts' 'loans'\n",
            " 'insurance' 'cards' 'insurance' 'cards' 'cards' 'loans' 'security'\n",
            " 'accounts' 'insurance' 'insurance' 'loans' 'insurance' 'insurance'\n",
            " 'insurance' 'insurance' 'insurance' 'insurance' 'insurance' 'insurance'\n",
            " 'insurance' 'insurance' 'insurance' 'loans' 'insurance' 'accounts'\n",
            " 'accounts' 'insurance' 'accounts' 'insurance' 'insurance' 'insurance'\n",
            " 'accounts' 'loans' 'loans' 'cards' 'insurance' 'accounts' 'loans' 'cards'\n",
            " 'insurance' 'accounts' 'cards' 'accounts' 'insurance' 'cards' 'insurance'\n",
            " 'cards' 'insurance' 'accounts' 'accounts' 'insurance' 'loans' 'insurance'\n",
            " 'insurance' 'cards' 'insurance' 'cards' 'cards' 'insurance' 'loans'\n",
            " 'insurance' 'cards' 'cards' 'cards' 'loans' 'cards' 'cards' 'cards'\n",
            " 'insurance' 'loans' 'cards' 'insurance' 'insurance' 'insurance'\n",
            " 'insurance' 'insurance' 'accounts' 'loans' 'insurance' 'insurance'\n",
            " 'loans' 'accounts' 'insurance' 'insurance' 'insurance' 'cards'\n",
            " 'insurance' 'loans' 'cards' 'cards' 'loans' 'cards' 'insurance'\n",
            " 'insurance' 'cards' 'cards' 'insurance' 'accounts' 'loans' 'insurance'\n",
            " 'insurance' 'cards' 'accounts' 'insurance' 'cards' 'cards' 'cards'\n",
            " 'insurance' 'insurance' 'insurance' 'insurance' 'insurance' 'cards'\n",
            " 'loans' 'insurance' 'cards' 'loans' 'insurance' 'cards' 'cards' 'cards'\n",
            " 'insurance' 'loans' 'insurance' 'loans' 'accounts' 'insurance' 'accounts'\n",
            " 'loans' 'loans' 'cards' 'accounts' 'accounts' 'insurance' 'insurance'\n",
            " 'cards' 'accounts' 'cards' 'cards' 'loans' 'cards' 'accounts' 'loans'\n",
            " 'cards' 'insurance' 'cards' 'insurance' 'cards' 'insurance' 'accounts'\n",
            " 'insurance' 'loans' 'loans' 'insurance' 'cards' 'insurance' 'insurance'\n",
            " 'cards' 'cards' 'loans' 'accounts' 'insurance' 'accounts' 'insurance'\n",
            " 'accounts' 'accounts' 'cards' 'accounts' 'accounts' 'loans' 'insurance'\n",
            " 'accounts' 'cards' 'insurance' 'cards' 'loans' 'loans' 'loans' 'cards'\n",
            " 'insurance' 'loans' 'insurance' 'cards' 'insurance' 'insurance'\n",
            " 'insurance' 'insurance' 'accounts' 'loans' 'cards' 'cards' 'accounts'\n",
            " 'accounts' 'accounts' 'insurance' 'accounts' 'accounts' 'cards'\n",
            " 'insurance' 'cards' 'insurance' 'loans' 'insurance' 'loans' 'insurance'\n",
            " 'insurance' 'cards' 'loans' 'loans' 'insurance' 'insurance' 'insurance'\n",
            " 'cards' 'insurance' 'accounts' 'accounts' 'insurance' 'insurance' 'loans'\n",
            " 'accounts' 'insurance' 'insurance' 'insurance' 'insurance' 'cards'\n",
            " 'insurance' 'cards' 'loans' 'insurance' 'insurance' 'insurance'\n",
            " 'insurance' 'insurance' 'accounts']\n",
            "1107      insurance\n",
            "212           loans\n",
            "1725          cards\n",
            "1518          cards\n",
            "1296    investments\n",
            "           ...     \n",
            "265           loans\n",
            "611        accounts\n",
            "1100      insurance\n",
            "1280    investments\n",
            "598        accounts\n",
            "Name: Class, Length: 353, dtype: object\n"
          ]
        }
      ],
      "source": [
        "svm_accuracy = accuracy_score(y_test, svm_predictions)\n",
        "print(svm_predictions)\n",
        "print(y_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SmZkcYhKPBz0",
        "outputId": "50a1e889-18e6-4878-8696-c081e8d2f872"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "SVM accuracy: 0.7620396600566572\n"
          ]
        }
      ],
      "source": [
        "print(\"SVM accuracy:\", svm_accuracy)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 466
        },
        "id": "cSKAj988Pg_5",
        "outputId": "ab6d67b5-14df-4c5a-9a36-dc3b571c8dfd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "SVM confusion matrix:\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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oefvTERERDoKgR7bpFKpMHPmTL11UVFRmDFjRqn7b926FWfOnMFvv/321LbU1FRYWFjA3t5eb72zszNSU8v+Mr8yFxL/zMns2LFjmQ9OREREwt3+GRkZifBw/SfT/tuzk27duoVx48bh4MGDot4mbNBkS6knixAREVVFQn1/KpXKMj90MTExEffv38dLL72kW1dSUoKjR49i+fLlOHDgAIqKipCVlaXXK5GWlgYXF5cyZzKokPD09HzuH8bDh/J4dzwREVFV1qVLF/z5559664YMGQJvb29MmjQJdevWhbm5OeLi4tC7d28AQHJyMlJSUhAYGFjm8xhUSMycOfOpJ1sSERHRs0nxQCobGxv4+fnpratevTqcnJx064cOHYrw8HA4OjrC1tYWY8eORWBgIAICAsp8HoMKif79+6NWrVqGfISIiOiFV1kfkb148WKYmJigd+/eeg+kMkSZCwnOjyAiIqraDh8+rPezpaUlVqxYgRUrVhh9TIPv2iAiIiLDyPkf42UuJJ58NTERERGVjYlAz5GojOTbMiIiIhKd/F/rRkREJDEObRAREZHR5FxIcGiDiIiIjMYeCSIiIpGZSPBAqorCQoKIiEhkch7aYCFBREQkssr6ZEshcI4EERERGU2WPRL5j3OljiC6ambWUkegckrculPqCKIr0T6WOoLoTBWy/GuUBCbFS7sqCv8LICIiEpmJQr4DAPJtGREREYmOPRJEREQi410bREREZDQ5z5Hg0AYREREZjT0SREREIpPzcyRYSBAREYmMQxtEREREpWCPBBERkcg4tEFERERGU8j4gVQsJIiIiETGORJEREREpWCPBBERkcg4R4KIiIiMJudHZHNog4iIiIzGHgkiIiKRmch4siULCSIiIpFxaIOIiIioFOyRICIiEhkfSEVERERGk/McCfmWSERERCQ69kiUw/20B1i5JAYnjyegsLAQderWwdTZkfBp4i11NEFtjd2GTes3IT09A55enpg8ZRKaNvOTOpZg5NS+i7//he9j9+Fa8g1kpWchXPUh2nRspdue9TAbX6/cjrOnziH/UT68W3hhcPhAuNZ1kTB1+axfuwG/HDyEG9dvQmmpRPMWzfBh+BjU96gvdTTByel3tTRybh8nW9JTcnIeYUToaJiZmWHRys/w9a4t+DAiDDa2NlJHE9T+fQewYN5CjBg9Alt3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u7u7hMmEExYWhtjYWHz33XewsbHRzW+xs7ODlZWVxOnKLzIyEt26dYO7uzsePXqE2NhYHD58GAcOHJA6mmBsbGyemtNSvXp1ODk5yWauS0REBLp374569erh7t27iIqKgqmpKd555x2powliwoQJePnllzF37lz07dsXp06dwpo1a7BmzRqpo1FZSH3bSFW3bNkyrbu7u9bCwkLbtm1bbXx8vNSRBHPo0CEtgKeW0NBQqaMJprT2AdBu2LBB6miCeP/997X16tXTWlhYaGvWrKnt0qWL9qeffpI6lujkdvtnv379tK6urloLCwtt7dq1tf369dNeuXJF6liC2rt3r9bPz0+rVCq13t7e2jVr1kgdicqIrxEnIiIio3GOBBERERmNhQQREREZjYUEERERGY2FBBERERmNhQQREREZjYUEERERGY2FBBERERmNhQQREREZjYUEkQwNHjwYPXr00P386quvYvz48RWe4/Dhw1AoFMjKyqrwcxNRxWAhQVSBBg8eDIVCAYVCoXsr56xZs/D48WNRz/vtt99i9uzZZdqXX/5EZAi+tIuognXt2hUbNmyAWq3Gjz/+iLCwMJibmyMyMlJvv6KiIlhYWAhyTkdHR0GOQ0T0JPZIEFUwpVIJFxcX1KtXD6NGjUJQUBD27NmjG4749NNP4ebmBi8vLwDArVu30LdvX9jb28PR0REhISG4ceOG7nglJSUIDw+Hvb09nJyc8PHHH+PJV+g8ObShVqsxadIk1K1bF0qlEo0aNcK6detw48YNdOrUCQDg4OAAhUKBwYMHA/j79eMqlQoeHh6wsrJC8+bNsXPnTr3z/Pjjj/D09ISVlRU6deqkl5OI5ImFBJHErKysUFRUBACIi4tDcnIyDh48iO+//x7FxcUIDg6GjY0Njh07hl9//RXW1tbo2rWr7jMLFy7Exo0bsX79ehw/fhwPHz7Erl27nnnO9957D19//TU+//xzXLx4EatXr4a1tTXq1q2Lb775BgCQnJyMe/fuYenSpQAAlUqFzZs3Y9WqVTh//jwmTJiAgQMH4siRIwD+Lnh69eqF7t27IykpCR988AEmT54s1h8bEVUWEr99lOiFEhoaqg0JCdFqtVqtRqPRHjx4UKtUKrURERHa0NBQrbOzs1atVuv237Jli9bLy0ur0Wh069RqtdbKykp74MABrVar1bq6umrnz5+v215cXKytU6eO7jxarf5rtZOTk7UAtAcPHiw14z+vj8/MzNStKyws1FarVk174sQJvX2HDh2qfeedd7RarVYbGRmp9fX11ds+adKkp45FRPLCORJEFez777+HtbU1iouLodFo8O6772LGjBkICwtD06ZN9eZF/PHHH7hy5QpsbGz0jlFYWIirV68iOzsb9+7dg7+/v26bmZkZWrdu/dTwxj+SkpJgamqKjh07ljnzlStXkJ+fj9dee01vfVFREVq2bAkAuHjxol4OAAgMDCzzOYioamIhQVTBOnXqhJiYGFhYWMDNzQ1mZv/9z7B69ep6++bm5qJVq1b46quvnjpOzZo1jTq/lZWVwZ/Jzc0FAPzwww+oXbu23jalUmlUDiKSBxYSRBWsevXqaNSoUZn2femll7Bt2zbUqlULtra2pe7j6uqKhIQEvPLKKwCAx48fIzExES+99FKp+zdt2hQajQZHjhxBUFDQU9v/6REpKSnRrfP19YVSqURKSsq/9mT4+Phgz549euvi4+Of30giqtI42ZKoEhswYABq1KiBkJAQHDt2DNevX8fhw4fx4Ycf4vbt2wCAcePGITo6Grt378Zff/2F0aNHP/MZEPXr10doaCjef/997N69W3fM7du3AwDq1asHhUKB77//Hg8ePEBubi5sbGwQERGBCRMmYNOmTbh69SrOnDmDZcuWYdOmTQCAkSNH4vLly5g4cSKSk5MRGxuLjRs3iv1HREQSYyFBVIlVq1YNR48ehbu7O3r16gUfHx8MHToUhYWFuh6Kjz76CIMGDUJoaCgCAwNhY2ODnj17PvO4MTExePvttzF69Gh4e3tj2LBhyMvLAwDUrl0bM2fOxOTJk+Hs7IwxY8YAAGbPno1p06ZBpVLBx8cHXbt2xQ8//AAPDw8AgLu7O7755hvs3r0bzZs3x6pVqzB37lwR/3SIqDJQaP9tRhYRERHRc7BHgoiIiIzGQoKIiIiMxkKCiIiIjMZCgoiIiIzGQoKIiIiMxkKCiIiIjMZCgoiIiIzGQoKIiIiMxkKCiIiIjMZCgoiIiIzGQoKIiIiM9n8xOLoKdbz1hgAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "print(\"SVM confusion matrix:\")\n",
        "cm=(confusion_matrix(y_test, svm_predictions))\n",
        "#create a heatmap of the confusion matrix\n",
        "sns.heatmap(cm, annot=True, fmt='g', cmap='Greens')\n",
        "plt.xlabel('Predicted')\n",
        "plt.ylabel('True')\n",
        "plt.show()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aVz92Kb8Qt4m",
        "outputId": "e30bdd29-cc29-4bc7-d2ec-718f4d4c4cc8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "SVM classification report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "     accounts       0.85      0.88      0.86        57\n",
            "        cards       0.95      0.84      0.89        88\n",
            "fundstransfer       0.00      0.00      0.00         6\n",
            "    insurance       0.55      0.98      0.70        86\n",
            "  investments       1.00      0.07      0.14        27\n",
            "        loans       0.97      0.70      0.81        81\n",
            "     security       1.00      0.25      0.40         8\n",
            "\n",
            "     accuracy                           0.76       353\n",
            "    macro avg       0.76      0.53      0.54       353\n",
            " weighted avg       0.83      0.76      0.74       353\n",
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n",
            "/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n",
            "/usr/local/lib/python3.11/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"
          ]
        }
      ],
      "source": [
        "print(\"SVM classification report:\")\n",
        "print(classification_report(y_test, svm_predictions))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "id": "A7KGUm9MRA6V"
      },
      "outputs": [],
      "source": [
        "# Applying Navie Bayes Algorithm\n",
        "from sklearn.naive_bayes import MultinomialNB\n",
        "from sklearn.model_selection import GridSearchCV"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Tvu39k7lRs6n",
        "outputId": "25487e14-5967-45f2-91ea-07aabcee305c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 0.9065155807365439\n"
          ]
        }
      ],
      "source": [
        "# define the hyperparameter grid to search\n",
        "param_grid = {\n",
        "    'alpha': [0.01, 0.1, 0.5, 1.0, 2.0],\n",
        "    'fit_prior': [True, False],\n",
        "}\n",
        "\n",
        "#Create the Multinomial Nsvie Bayes Model\n",
        "mnd = MultinomialNB()\n",
        "#perform grid search with cross_validation\n",
        "grid_search = GridSearchCV(mnd, param_grid=param_grid, cv=5, scoring='accuracy')\n",
        "grid_search.fit(X_train, y_train)\n",
        "#Get the best model and make predictions on the test set\n",
        "best_model = grid_search.best_estimator_\n",
        "y_pred = best_model.predict(X_test)\n",
        "#Calculate the accuracy score\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "print(\"Accuracy:\", accuracy)\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9t_uoGJHVCMr",
        "outputId": "98c10dda-85bf-4279-a4e9-2cb928c55d63"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['insurance' 'loans' 'cards' 'cards' 'investments' 'insurance' 'cards'\n",
            " 'investments' 'insurance' 'accounts' 'cards' 'loans' 'insurance'\n",
            " 'insurance' 'investments' 'loans' 'accounts' 'cards' 'loans' 'loans'\n",
            " 'fundstransfer' 'loans' 'insurance' 'loans' 'insurance' 'accounts'\n",
            " 'loans' 'loans' 'cards' 'cards' 'insurance' 'cards' 'accounts'\n",
            " 'insurance' 'loans' 'loans' 'insurance' 'security' 'insurance' 'loans'\n",
            " 'insurance' 'loans' 'cards' 'investments' 'fundstransfer' 'loans' 'cards'\n",
            " 'cards' 'cards' 'loans' 'cards' 'accounts' 'accounts' 'cards'\n",
            " 'investments' 'accounts' 'investments' 'loans' 'cards' 'insurance'\n",
            " 'investments' 'security' 'insurance' 'accounts' 'cards' 'investments'\n",
            " 'insurance' 'insurance' 'insurance' 'cards' 'insurance' 'insurance'\n",
            " 'cards' 'loans' 'insurance' 'investments' 'loans' 'loans' 'investments'\n",
            " 'cards' 'insurance' 'insurance' 'accounts' 'accounts' 'cards'\n",
            " 'investments' 'accounts' 'insurance' 'insurance' 'investments' 'loans'\n",
            " 'cards' 'investments' 'insurance' 'loans' 'accounts' 'cards' 'insurance'\n",
            " 'loans' 'accounts' 'loans' 'insurance' 'accounts' 'loans' 'cards'\n",
            " 'accounts' 'cards' 'insurance' 'cards' 'insurance' 'investments'\n",
            " 'accounts' 'cards' 'loans' 'fundstransfer' 'insurance' 'insurance'\n",
            " 'loans' 'loans' 'accounts' 'cards' 'loans' 'cards' 'cards' 'loans'\n",
            " 'security' 'accounts' 'insurance' 'loans' 'loans' 'insurance'\n",
            " 'investments' 'accounts' 'insurance' 'accounts' 'security' 'loans'\n",
            " 'loans' 'insurance' 'insurance' 'loans' 'loans' 'cards' 'accounts'\n",
            " 'accounts' 'insurance' 'investments' 'insurance' 'insurance' 'insurance'\n",
            " 'accounts' 'loans' 'loans' 'cards' 'insurance' 'accounts' 'loans' 'cards'\n",
            " 'insurance' 'accounts' 'cards' 'investments' 'insurance' 'cards' 'loans'\n",
            " 'cards' 'investments' 'accounts' 'accounts' 'investments' 'loans'\n",
            " 'insurance' 'cards' 'cards' 'investments' 'cards' 'cards' 'insurance'\n",
            " 'loans' 'insurance' 'cards' 'cards' 'cards' 'loans' 'cards' 'cards'\n",
            " 'cards' 'insurance' 'loans' 'cards' 'insurance' 'accounts' 'security'\n",
            " 'loans' 'insurance' 'accounts' 'loans' 'insurance' 'insurance' 'loans'\n",
            " 'accounts' 'cards' 'insurance' 'insurance' 'cards' 'cards' 'loans'\n",
            " 'cards' 'cards' 'loans' 'security' 'insurance' 'insurance' 'cards'\n",
            " 'cards' 'investments' 'accounts' 'loans' 'insurance' 'loans' 'cards'\n",
            " 'accounts' 'insurance' 'cards' 'cards' 'cards' 'insurance' 'insurance'\n",
            " 'insurance' 'insurance' 'insurance' 'cards' 'loans' 'cards' 'cards'\n",
            " 'loans' 'cards' 'cards' 'cards' 'cards' 'investments' 'loans' 'loans'\n",
            " 'loans' 'accounts' 'insurance' 'accounts' 'loans' 'loans' 'cards'\n",
            " 'accounts' 'accounts' 'accounts' 'fundstransfer' 'cards' 'accounts'\n",
            " 'cards' 'cards' 'loans' 'cards' 'investments' 'loans' 'cards' 'loans'\n",
            " 'cards' 'insurance' 'cards' 'insurance' 'accounts' 'insurance' 'loans'\n",
            " 'loans' 'cards' 'security' 'investments' 'insurance' 'cards' 'cards'\n",
            " 'loans' 'accounts' 'insurance' 'investments' 'insurance' 'accounts'\n",
            " 'accounts' 'cards' 'accounts' 'accounts' 'loans' 'insurance' 'accounts'\n",
            " 'cards' 'investments' 'cards' 'loans' 'loans' 'loans' 'cards' 'loans'\n",
            " 'loans' 'insurance' 'cards' 'investments' 'insurance' 'cards' 'security'\n",
            " 'investments' 'loans' 'cards' 'cards' 'security' 'accounts' 'accounts'\n",
            " 'investments' 'accounts' 'accounts' 'cards' 'insurance' 'cards'\n",
            " 'insurance' 'loans' 'insurance' 'loans' 'loans' 'loans' 'cards' 'loans'\n",
            " 'loans' 'insurance' 'cards' 'insurance' 'cards' 'insurance' 'accounts'\n",
            " 'accounts' 'accounts' 'insurance' 'loans' 'accounts' 'investments'\n",
            " 'insurance' 'insurance' 'insurance' 'accounts' 'insurance' 'cards'\n",
            " 'loans' 'security' 'insurance' 'insurance' 'insurance' 'loans' 'accounts']\n"
          ]
        }
      ],
      "source": [
        "nb_predictions = best_model.predict(X_test)\n",
        "print( nb_predictions)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "waZkgXRCVNMd",
        "outputId": "6287712f-0a7e-4ec5-dbcb-8ed21b7b1326"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<function accuracy_score at 0x793142b207c0>\n"
          ]
        }
      ],
      "source": [
        "nb_accuracy = accuracy_score(y_test, nb_predictions)\n",
        "print(accuracy_score)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FP4PBKCnVzqd",
        "outputId": "ffc33455-1bb3-405c-96e4-3fa64bb365f8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Navie Bayes accuracy: 0.9065155807365439\n"
          ]
        }
      ],
      "source": [
        "print(\"Navie Bayes accuracy:\", nb_accuracy)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 466
        },
        "id": "0VE5Y7QNWDbW",
        "outputId": "962d5ce6-cf57-4d06-f41c-7d8d31cdc495"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Navie Bayes confusion matrix:\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "print(\"Navie Bayes confusion matrix:\")\n",
        "cm=(confusion_matrix(y_test, nb_predictions))\n",
        "sns.heatmap(cm, annot=True, fmt='g', cmap='Greens')\n",
        "plt.xlabel('Predicted')\n",
        "plt.ylabel('True')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bltcdl32XBI9",
        "outputId": "8fb1b975-bd75-4603-d3bf-86bd379b61a2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Navie Bayes classification report:\n",
            "               precision    recall  f1-score   support\n",
            "\n",
            "     accounts       0.91      0.88      0.89        57\n",
            "        cards       0.93      0.94      0.94        88\n",
            "fundstransfer       1.00      0.67      0.80         6\n",
            "    insurance       0.92      0.92      0.92        86\n",
            "  investments       0.80      0.89      0.84        27\n",
            "        loans       0.94      0.91      0.93        81\n",
            "     security       0.60      0.75      0.67         8\n",
            "\n",
            "     accuracy                           0.91       353\n",
            "    macro avg       0.87      0.85      0.85       353\n",
            " weighted avg       0.91      0.91      0.91       353\n",
            "\n"
          ]
        }
      ],
      "source": [
        "#Print the classification report and confusion matrix for Navie Bayes model\n",
        "print(\"Navie Bayes classification report:\")\n",
        "print(classification_report(y_test, nb_predictions))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LKqpUPThYGwK",
        "outputId": "df0f382a-b6a5-419b-bb92-d30cf6d342a1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Predicted class: cards\n",
            "Predicted answer: Welcome Benefit 500 Times Points will be gifted after you use the card to shop for the first times. Earn Times Points every time you shop. Get 2 Times Points for every Rs. 150 spent. Earn Times Points based on the activities on the Times Internet Limited digital pages. The list of Times Internet Limited digital properties are www.timesofindia.com, www.speakingtree.in, www.economictimes.com , www.itimes.com , www.maharashtratimes.com , www.eisamay.com , www.gaana.com , www.navgujratsamay.com , www.navbharattimes.com Please note, you need to be logged in to your Times Points account for earning Times Points while consuming, sharing & creating content on above listed websites.\n"
          ]
        }
      ],
      "source": [
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "input_question = \"How can I earn Times Points\"\n",
        "input_vector = vectorizer.transform([input_question])\n",
        "predicted_class = best_model.predict(input_vector)[0]\n",
        "class_data = df[df['Class'] == predicted_class]\n",
        "class_vectors = vectorizer.transform(class_data['Question'])\n",
        "similarities = cosine_similarity(input_vector, class_vectors)\n",
        "most_similar_index = similarities.argmax()\n",
        "predicted_answer = class_data.iloc[most_similar_index]['Answer']\n",
        "# Print the predicted class and answer\n",
        "print(\"Predicted class:\", predicted_class)\n",
        "print(\"Predicted answer:\", predicted_answer)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ac2z_zw-Xw4o",
        "outputId": "6ae5e89e-ffc7-4479-a07d-e783bbb4ccfd"
      },
      "execution_count": None,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.42.2-py2.py3-None-any.whl.metadata (8.9 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.1)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.25.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (13.9.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-None-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-None-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.5)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.27.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.1)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.1.31)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.42.2-py2.py3-None-any.whl (9.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.6/9.6 MB\u001b[0m \u001b[31m58.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-None-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m85.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-None-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m6.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.42.2 watchdog-6.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "print(\"Streamlit is installed successfully!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9W25zB1VXfn6",
        "outputId": "08c64bd5-f400-4179-b2d4-90aa1b7ec5e7"
      },
      "execution_count": None,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Streamlit is installed successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Streamlit UI setup\n",
        "st.set_page_config(page_title=\"Banking Chatbot\", page_icon=\"🤖\")\n",
        "st.title(\"How can I help you?\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J84FM-ClvFWj",
        "outputId": "6b28e4ec-9f6e-4f3b-d846-31b59b27517f"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-02-24 06:54:33.001 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 06:54:33.003 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 06:54:33.004 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9R8Z1xsKbh9S",
        "outputId": "022e9d8c-5b9d-4b52-cbd9-951da320248a"
      },
      "execution_count": None,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Usage: streamlit run [OPTIONS] TARGET [ARGS]...\n",
            "Try 'streamlit run --help' for help.\n",
            "\n",
            "Error: Invalid value: File does not exist: app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from sklearn.feature_extraction.text import CountVectorizer\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "from sklearn.svm import SVC\n",
        "\n",
        "#Load the data from CSV file\n",
        "data = pd.read_csv(\"/BankFAQs.csv\")\n",
        "\n",
        "#Define the vectorizer\n",
        "vectorizer = CountVectorizer()\n",
        "#Transform the text data into feature vectors\n",
        "X = vectorizer.fit_transform(data['Question'])\n",
        "\n",
        "# Define the labels\n",
        "y = data['Class']\n",
        "\n",
        "#Train the SVM model\n",
        "svm_model = SVC(C=10, kernel='rbf', gamma=0.1, decision_function_shape='ovr')\n",
        "svm_model.fit(X, y)\n",
        "\n",
        "#Define the Streamlit app\n",
        "st.set_page_config(page_title=\"Banking-Chatbot\", page_icon=\": robot:\")\n",
        "\n",
        "#Add a title\n",
        "st.title(\"How can i help you?\")\n",
        "\n",
        "#Create a session state to persist data across user interactions\n",
        "session_state = st.session_state\n",
        "if not hasattr(session_state, 'previous_qa'):\n",
        "    session_state.previous_qa = []\n",
        "\n",
        "\n",
        "#Button to clear the history\n",
        "clear_history = st.checkbox(\"Clear Chat History\", key=\"clear_history_checkbox\")\n",
        "\n",
        "#Display chat history\n",
        "st.header(\"Chat History\")\n",
        "\n",
        "# Display previous conversations in a more visually appealing way\n",
        "for qa in session_state.previous_qa:\n",
        "    st.markdown(\n",
        "        f\"<div style='background-color:#f2f2f2; padding:10px; border-radius:10px; margin-bottom:10px;'>\"\n",
        "        f\"<p style='font-weight:bold; color:#1f405d; '>User: {qa['User']}</p>\"\n",
        "        f\"<p style='color:#4d4d4d;'>Bot: {qa['Bot']}</p>\"\n",
        "        f\"</div>\",\n",
        "        unsafe_allow_html=True\n",
        "    )\n",
        "\n",
        "# get user input at the bottom of the page\n",
        "user_input = st.text_input(\"You:\", key=\"user_input\")\n",
        "\n",
        "#Make predections\n",
        "if user_input:\n",
        "  if clear_history:\n",
        "    #cleart the chart history if the user wants to clear it\n",
        "    session_state.previous_qa = []\n",
        "\n",
        "  # Transfrom the input question into a feature vector\n",
        "  input_vector = vectorizer.transform([user_input])\n",
        "\n",
        "  # Predict the class of the input question\n",
        "  predicted_class = svm_model.predict(input_vector)[0]\n",
        "\n",
        "  # Find the answer of the predicted class that is most similar to the input question\n",
        "  class_data = data[data['Class'] == predicted_class]\n",
        "  class_vectors = vectorizer.transform(class_data['Question'])\n",
        "  similarities = cosine_similarity(input_vector, class_vectors)\n",
        "  most_similar_index = similarities.argmax()\n",
        "  predicted_answer = class_data.iloc[most_similar_index]['Answer']\n",
        "\n",
        "  # Display the user question and bot answer in the chart history\n",
        "  session_state.previous_qa.append({\"User\": user_input, \"Bot\": predicted_answer})\n",
        "\n",
        "  # Display the predicted answer from the bot in a more visually appealing way\n",
        "  st.markdown(\n",
        "      f\"<div style='background-color:#f2f2f2; padding:10px; border-radius:10px; margin-bottom:10px;'>\"\n",
        "      f\",<p style='font-weight:bold; color:#1f405d; '>Bot: {predicted_answer}</p>\"\n",
        "      f\"</div>\",\n",
        "      unsafe_allow_html=True\n",
        "  )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NzvJTkAEZb7W",
        "outputId": "fce37d24-683a-423e-f24c-c0487f392915"
      },
      "execution_count": None,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-02-24 05:36:39.328 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.331 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.334 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.338 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.341 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.344 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.347 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.348 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.352 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.354 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.355 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.358 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.360 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.362 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.363 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.365 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.366 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 05:36:39.368 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "adcUAoyhNWfa"
      },
      "execution_count": None,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNGBCoQ5dMgJIOHiDTVZp6y",
      "include_colab_link": True
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
