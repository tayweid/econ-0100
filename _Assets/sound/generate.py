"""Regenerate the dogfood click sounds. Deterministic: same seed, same waves.

python generate.py  ->  writes the .wav files next to this script.

Each sound is a micro-impact recipe: high-passed noise burst (the strike)
+ a resonant tick (the mechanism ringing) + a low damped sine (the thock),
each with its own decay. Sharpness lives in the decay taus and hp_passes;
brightness in tick_hz and the sparkle partial. tick-glass-a/b are the
watch-dial detent picks (2026-08-22): glass's 4.6-4.9 kHz body with the
needle-fast attack (triple high-pass, no smoothing).
"""
import os
import wave

import numpy as np

SR = 48000
OUT = os.path.dirname(os.path.abspath(__file__))


def transient(rng, dur, tick_hz, tick_tau, noise_tau, thump_hz, thump_tau,
              mix, hp_passes=1, sparkle_hz=None, sparkle_tau=0.0006,
              sparkle_amp=0.35):
    n = int(SR * dur)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    for _ in range(hp_passes):
        noise = np.diff(noise, prepend=0.0)
    body = noise / np.max(np.abs(noise)) * np.exp(-t / noise_tau)
    tick = np.sin(2 * np.pi * tick_hz * t) * np.exp(-t / tick_tau)
    thump = np.sin(2 * np.pi * thump_hz * t) * np.exp(-t / thump_tau)
    w_body, w_tick, w_thump = mix
    out = w_body * body + w_tick * tick + w_thump * thump
    if sparkle_hz:
        out += sparkle_amp * np.sin(2 * np.pi * sparkle_hz * t) * np.exp(-t / sparkle_tau)
    return out


def finish(parts, total, smooth_taps=1, peak=0.5):
    """parts: list of (offset_seconds, amplitude, signal)."""
    out = np.zeros(int(SR * total))
    for offset, amp, sig in parts:
        i = int(SR * offset)
        out[i:i + len(sig)] += amp * sig[:len(out) - i]
    if smooth_taps > 1:
        k = np.hanning(smooth_taps)
        k /= k.sum()
        out = np.convolve(out, k, mode="same")
    out = out / np.max(np.abs(out)) * peak
    fade = int(SR * 0.008)
    out[-fade:] *= np.linspace(1, 0, fade)
    return out


def write(name, signal):
    path = os.path.join(OUT, f"{name}.wav")
    with wave.open(path, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SR)
        f.writeframes((signal * 32767).astype(np.int16).tobytes())
    return path


def main():
    rng = np.random.default_rng(7)

    # crown detent: engage + settle, 7 ms apart
    click = finish([
        (0.000, 1.00, transient(rng, dur=0.020, tick_hz=2300, tick_tau=0.0015,
                                noise_tau=0.003, thump_hz=210, thump_tau=0.006,
                                mix=(0.8, 0.5, 0.35))),
        (0.007, 0.55, transient(rng, dur=0.020, tick_hz=2600, tick_tau=0.0012,
                                noise_tau=0.002, thump_hz=210, thump_tau=0.006,
                                mix=(0.8, 0.5, 0.35))),
    ], total=0.09, smooth_taps=9)

    # camera-dial / rotary-switch: chunkier, lower
    clack = finish([
        (0.000, 1.00, transient(rng, dur=0.026, tick_hz=1500, tick_tau=0.0022,
                                noise_tau=0.004, thump_hz=140, thump_tau=0.010,
                                mix=(0.7, 0.45, 0.6))),
        (0.009, 0.45, transient(rng, dur=0.018, tick_hz=1900, tick_tau=0.0015,
                                noise_tau=0.003, thump_hz=140, thump_tau=0.006,
                                mix=(0.7, 0.45, 0.6))),
    ], total=0.11, smooth_taps=9)

    # the watch-dial picks: glass body, needle attack
    glass_a = finish([
        (0.0, 1.0, transient(rng, dur=0.009, tick_hz=4600, tick_tau=0.0007,
                             noise_tau=0.0008, thump_hz=300, thump_tau=0.0022,
                             mix=(0.75, 0.55, 0.07), hp_passes=3,
                             sparkle_hz=7200, sparkle_tau=0.0005)),
    ], total=0.045)

    glass_b = finish([
        (0.0, 1.0, transient(rng, dur=0.008, tick_hz=4900, tick_tau=0.0006,
                             noise_tau=0.0007, thump_hz=310, thump_tau=0.002,
                             mix=(0.8, 0.5, 0.06), hp_passes=3,
                             sparkle_hz=8000, sparkle_tau=0.00045,
                             sparkle_amp=0.4)),
    ], total=0.04, peak=0.55)

    for name, sig in [("click", click), ("clack", clack),
                      ("tick-glass-a", glass_a), ("tick-glass-b", glass_b)]:
        print(write(name, sig))


if __name__ == "__main__":
    main()
