# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import numpy as np
import librosa
import torchaudio
import torch
from torch.nn import DataParallel

class MusicGenerator:
    def __init__(self, model_path="facebook/musicgen-medium"):
        self.model_name = model_path
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        self.processor = AutoProcessor.from_pretrained(self.model_name)
        self.model = MusicgenForConditionalGeneration.from_pretrained(self.model_name)
        
        if torch.cuda.device_count() > 1:
            print(f"Using {torch.cuda.device_count()} GPUs!")
            self.model = DataParallel(self.model)
        
        self.model.to(self.device)

    def generate_music(self, prompt):
        try:
            inputs = self.processor(
                text=[prompt],
                padding=True,
                return_tensors="pt",
            ).to(self.device)
            audio_values = self.model.generate(**inputs, max_new_tokens=750)
            # Handle the output based on whether the model is wrapped by DataParallel
            if isinstance(self.model, DataParallel):
                audio_values = audio_values[0]  # Adjusting the output tensor accordingly
            return audio_values.cpu().numpy()
        except Exception as e:
            print(f"An error occurred with {self.model_name}: {e}")
            return None
