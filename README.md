# Audio Generation Subnetwork

This subnetwork is a decentralized system designed for text-to-audio applications within the Bittensor network. It consists of a Validator and a Miner working collaboratively to generate high-quality audio from provided prompts. 
In the first phase, we will start with text-to-speech (TTS), working in parallel to add music generation in the upcoming updates. 

## Validators

The Validators are responsible for initiating the generation process by providing prompts to the Miners on the network. These prompts serve as the input text for the subsequent TTS model. The Validators evaluate the quality of the generated audio produced by the Miners and reward them based on the perceived quality.
Please refer to the [Validator Documentation](docs/validator.md).


## Miners

Miners in the Audio Subnetwork are tasked with generating audio from the text prompts received from the Validators. Leveraging advanced text-to-speech models, miners aim to produce high-fidelity, natural-sounding voice recordings. The quality of the generated audio is crucial, as it directly influences the miners' rewards.
Please refer to the [Miner Documentation](docs/miner.md).

## Workflow

1. **Prompt Generation:** The Validators generates prompts and distributes them to the Miners on the network.

2. **Text-to-Speech Processing:** Miners receive the prompts and utilize text-to-speech models to convert the text into voice audio.

3. **Quality Evaluation:** The Validator assesses the quality of the generated audio, considering factors such as: clarity, naturalness, and adherence to the prompt.

4. **Reward Distribution:** Based on the quality assessment, the Validator rewards Miners accordingly. Miners with consistently higher-quality outputs receive a larger share of rewards.

## Benefits

- **Decentralized Text-to-Speech:** The subnetwork decentralizes the TTS process, distributing the workload among participating Miners.
  
- **Quality Incentives:** The incentive mechanism encourages Miners to continually improve the quality of their generated voice audio.

- **Bittensor Network Integration:** Leveraging the Bittensor network ensures secure and transparent interactions between Validators and Miners.

Join the Audio Subnetwork and contribute to the advancement of decentralized text-to-speech / text-to-music technologies within the Bittensor ecosystem.


## Installation
```bash 
git clone https://github.com/UncleTensor/AudioSubnet.git
cd AudioSubnet
git checkout main
pip install -r requirements.txt
python -m pip install -e . 
wandb login
```

## Recommended GPU Configuration

For optimal performance, it is recommended to use NVIDIA GeForce RTX 3090 GPUs for both Validators and Miners.


**Evaluation Mechanism:**
The evaluation mechanism involves the validator querying miners on the network with random prompts and receiving text-to-speech responses. These responses are scored based on correctness, and the weights on the Bittensor network are updated accordingly. The scoring is conducted using a reward function from the lib module.

**Miner/Validator Hardware Specs:**
The hardware requirements for miners and validators vary depending on the complexity and resource demands of the selected text-to-speech models. Typically, a machine equipped with a capable CPU and GPU, along with sufficient VRAM and RAM, is necessary. The amount of disk space required will depend on the size of the models and any additional data.

**How to Run a Validator:**
To operate a validator, you need to run the validator.py script with the required command-line arguments. This script initiates the setup of Bittensor objects, establishes a connection to the network, queries miners, scores their responses, and updates weights accordingly.

**How to Run a Miner:**
To operate a miner, run the miner.py script with the necessary configuration. This process involves initializing Bittensor objects, establishing a connection to the network, and processing incoming text-to-speech requests.

**Text-to-Speech Models Supported:**
The code incorporates three text-to-speech models: Microsoft/speecht5_tts, Facebook/mms-tts-eng and SunoBark. However, the specific requirements for each model, including CPU, GPU VRAM, RAM, and disk space, are not explicitly stated in the provided code. To ascertain these requirements, it may be necessary to consult the documentation or delve into the implementation details of these models.

In general, the resource demands of text-to-speech models can vary significantly. Larger models often necessitate more powerful GPUs and additional system resources. It is advisable to consult the documentation or model repository for the specific requirements of each model. Additionally, if GPU acceleration is employed, having a compatible GPU with enough VRAM is typically advantageous for faster processing.


### Voice Clone Service
Run the validator with the following command, replacing `{wallet_name}`, `{hotkey_name}`, and `{huggingface_access_token}` with your wallet and hotkey names and HuggingFace access token. Place your audio files (e.g., `audio01.wav`) and text files with the corresponding name (e.g., `audio01.txt`) in the `vc_source` folder for custom voice cloning. Once the files are processed, they will be moved to `vc_processed` folder. The voice cloned output will be saved in the `vc_target` folder.

### Text-to-Speech (TTS) Service
- For prompts from HuggingFace, set your HuggingFace access token.
- For custom prompts, place a CSV file named `tts_prompts.csv` in the `tts_source` directory. Audio outputs will be stored in the `tts_target` directory.

## License
This repository is licensed under the MIT License.

## Benchmark Results

This section outlines the benchmarking results for the audio evaluation subnetwork across different NVIDIA GPUs: RTX 4090, A6000, H100, and A100. It focuses on Text-to-Speech (TTS), Voice Cloning (VC), and Music audio services.

### Benchmark Summary for NVIDIA GPUs

#### RTX 4090
| Service | Average Evaluation Time (seconds) | Duration of Audio (seconds) | Maximum Time (seconds) | Minimum Time (seconds) |
|---------|------------------------|-----------------------------|------------------------|------------------------|
| Music   | 11.56                  | 15                          | 12.38                  | 11.39                  |
| TTS     | 2.33                   | 30                          | 2.80                   | 2.28                   |

#### NVIDIA A6000
| Service | Average Evaluation Time (seconds) | Duration of Audio (seconds) | Maximum Time (seconds) | Minimum Time (seconds) |
|---------|------------------------|-----------------------------|------------------------|------------------------|
| Music   | 8.39                  | 15                          | 11.09                  | 6.73                  |
| TTS     | 2.25                   | 30                          | 2.35                   | 2.14                   |
| VC      | 2.12                   | 30                          | 2.15                   | 1.95                   |

#### NVIDIA H100
| Service | Average Evaluation Time (seconds) | Duration of Audio (seconds) | Maximum Time (seconds) | Minimum Time (seconds) |
|---------|------------------------|-----------------------------|------------------------|------------------------|
| Music   | 5.80                   | 15                          | 7.18                   | 5.65                   |
| TTS     | 1.25                   | 30                          | 2.14                   | 1.04                   |
| VC      | 1.30                   | 30                          | 1.36                   | 1.16                   |

#### NVIDIA A100
| Service | Average Evaluation Time (seconds) | Duration of Audio (seconds) | Maximum Time (seconds) | Minimum Time (seconds) |
|---------|------------------------|-----------------------------|------------------------|------------------------|
| Music   | 7.12                   | 15                          | 8.26                   | 6.94                   |
| TTS     | 1.10                   | 30                          | 1.77                   | 1.01                   |
| VC      | 1.13                   | 30                          | 1.45                   | 1.01                   |

### Findings

- **Music Audio Evaluation**: The Evaluation varies across different GPUs, with the H100 and A100 GPUs showing higher efficiency by completing tasks in less time compared to their respective audio durations.
- **TTS and VC Audio Evaluation**: Exceptional efficiency is observed across all platforms for TTS and VC services, with tasks completing significantly faster than the duration of the audio, especially notable on the H100 and A100 GPUs.

These benchmark results demonstrate the high performance and efficiency of the Audio Evaluation across a range of high-performance NVIDIA GPUs, highlighting the network's capability for rapid and high-quality audio evaluation tasks within the ecosystem.


## Comprehensive Generation Task Benchmarks

This section summarizes the benchmarking results for generation tasks across four GPUs: A600, RTX 4090, A100, and H100. It covers Music Generation, Text to Speech (TTS), and Voice Cloning (VC) services, providing a comparative view of their performance.

### Benchmark Summary

| GPU Model | Service         | Average Time (s) | Maximum Time (s) | Minimum Time (s) | Duration of Audio (s) |
|-----------|-----------------|------------------|------------------|------------------|-----------------------|
| A6000      | Music Generation | 63.67            | 73.18            | 57.95            | 15                    |
| A6000      | Text To Speech   | 8.66             | 14.18            | 5.67             | 30                    |
| A6000      | Voice Clone      | 72.75            | 86.48            | 51.16            | 30                    |
| RTX 4090  | Music Generation | 52.92            | 73.18            | 29.43            | 15                    |
| RTX 4090  | Text To Speech   | 10.05            | 23.93            | 5.67             | 30                    |
| RTX 4090  | Voice Clone      | 74.17            | 182.47           | 14.10            | 30                    |
| A100      | Music Generation | 34.43            | 52.91            | 28.68            | 15                    |
| A100      | Text To Speech   | 5.11             | 6.92             | 3.74             | 30                    |
| A100      | Voice Clone      | 55.12            | 77.44            | 32.79            | 30                    |
| H100      | Music Generation | 34.18            | 56.71            | 30.26            | 15                    |
| H100      | Text To Speech   | 4.36             | 6.7              | 2.33             | 30                    |
| H100      | Voice Clone      | 82.15            | 113.92           | 50.37            | 30                    |

### Insights

The benchmarking results highlight the distinctive performance capabilities of each GPU model across the various audio generation tasks. The A100 and H100 GPUs show exceptional efficiency in Music Generation tasks, completing them in just over half the duration of the audio. Text to Speech tasks are efficiently handled across all GPU models, with particularly rapid synthesis times observed on the A100 and H100 GPUs. Voice Cloning presents a broader range of generation times due to its complexity, with the RTX 4090 showing the widest range but also the highest maximum time, indicative of its capability to handle particularly demanding cloning tasks.

These benchmarks provide valuable insights into the potential of each GPU within the Bittensor ecosystem, illustrating their strengths and capabilities in handling different types of audio synthesis tasks.

```text
MIT License

Copyright (c) 2024 Opentensor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```