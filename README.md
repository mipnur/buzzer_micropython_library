# 📢 MicroPython Passive Buzzer Library  
### Raspberry Pi Pico

This library allows you to control a **passive buzzer** using **MicroPython** on a  
**Raspberry Pi Pico**, generating sound through **PWM**.

Examples adapted specifically for Raspberry Pi Pico are included,  
along with the **datasheets of the transistor and the passive buzzer used**.

---

## 📦 Repository Contents

- `buzzer_lib.py` — Main library file
- `examples/` — Raspberry Pi Pico examples
- `datasheets/`
  - NPN transistor datasheet
  - Passive buzzer datasheet

---

## 🔧 Requirements

- Raspberry Pi Pico / Pico W
- MicroPython installed
- Passive buzzer (3–12 V, 16 Ω)
- NPN transistor
- **1 kΩ resistor**
- Breadboard and jumper wires

---

## 🔌 Hardware Connection

The buzzer **must not be connected directly** to a GPIO pin.  
An **NPN transistor** is used to safely drive the buzzer.

### Wiring

- Pico GPIO → **1 kΩ resistor** → Transistor base
- Transistor emitter → GND
- Transistor collector → Buzzer
- Buzzer → 5 V

---

## 🎼 Features

- PWM tone generation
- Melody playback
- Adjustable timing
- Predefined musical notes

---

## 🎵 Musical Notes

```python
do = 262; re = 294; mi = 330; fa = 349; sol = 392; la = 440; si = 494
do_= 277; re_= 311; fa_= 370; sol_= 415; la_= 466
