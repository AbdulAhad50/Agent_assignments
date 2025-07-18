# 🧙‍♂️ Game Master Agent (Fantasy Adventure Game)

This is a text-based fantasy adventure game powered by the **OpenAI Agents SDK** and **Gemini 1.5 Flash** (via `litellm`). The system simulates a dungeon-master-style game experience by dynamically switching between AI agents responsible for narration, combat, and inventory management.

---

### 🎮 What It Does

* Narrates an engaging fantasy story based on player input.
* Uses tools like `roll_dice()` for randomness and `generate_event()` for magical events.
* Dynamically hands off between:

  * **NarratorAgent** – story progression
  * **MonsterAgent** – combat & enemy handling
  * **ItemAgent** – inventory, loot & magical items

---

### 🧰 Tools Used

* `roll_dice(sides: int)`
  → Simulates a dice roll (default: 6-sided).

* `generate_event(location: str)`
  → Generates a mystical story event in a given location.

---

### 🧠 Agents

| Agent Name          | Purpose                                         |
| ------------------- | ----------------------------------------------- |
| **GameMasterAgent** | Master controller for game flow & handoffs      |
| **NarratorAgent**   | Tells the main story, reacts to choices         |
| **MonsterAgent**    | Manages battles using dice roll tool            |
| **ItemAgent**       | Grants items/rewards using event generator tool |

---

### 🚀 How to Run

#### 1. Prerequisites

Make sure you have:

* Python 3.9+
* `openai-agents` installed
  (Install via: `pip install openai-agents`)
* Gemini API key from Google AI Studio

---

#### 2. Replace Gemini API Key

Update this line in the code with your API key:

```python
api_key='YOUR_GEMINI_API_KEY'
```

---

#### 3. Run the Agent

```bash
python main.py
```

You’ll see an interactive fantasy game unfold in the terminal based on the initial prompt.

---

### 📄 Example Input

```text
"I enter the dark forest, sword in hand."
```

### 🧾 Example Output

```text
You step into the dark forest, a howl echoes in the distance. Suddenly, a goblin appears...
🎲 You rolled a 5! You swing your sword and strike!
💎 A glowing amulet drops. You pick it up.
```

---

### 🏗️ Powered By

* [OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview)
* [Google Gemini 1.5 Flash](https://aistudio.google.com/app)
