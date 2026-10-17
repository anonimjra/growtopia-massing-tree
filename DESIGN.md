# 🎨 TECHNICAL & UI/UX DESIGN SPECIFICATION (DESIGN.md)
## PROJECT: SURG-E MASSING TREE & RECURSIVE REVENUE ENGINE
**Theme**: Shonen Jump Comic / Manga Universe • **Engine**: Client-Side Reactive Web App

---

## 1. Visual Design System & Manga Tokens
Desain mengadopsi aesthetic yang seragam dengan portal **Science Station** dan **Display Block** yang telah dideploy sebelumnya.

### 1.1. Color Palette (CSS Variables)
```css
:root {
  /* Ink & Paper */
  --manga-ink: #111116;
  --manga-paper: #fffcf0;
  --manga-halftone: #e8e2cd;

  /* Shonen Accent Glows */
  --shonen-yellow: #ffde00;   /* Warning, Ticker, Highlight */
  --shonen-orange: #ff5500;   /* Secondary Accents */
  --shonen-red: #ff1f4b;      /* Critical Bottleneck, Tier 0 Surg-E */
  --shonen-cyan: #00f0ff;     /* Energy Glow, Fuel Pack Status */
  --shonen-blue: #00b4d8;     /* Hospital Bed Branch */
  --shonen-purple: #7209b7;   /* Puzzle Brick Branch */
  --shonen-green: #06d6a0;    /* Pure Profit, Confetti, Success */

  /* Comic Borders & Shadows */
  --comic-border: 3.5px solid #111116;
  --comic-border-sm: 2px solid #111116;
  --comic-shadow: 4px 4px 0 #111116;
  --comic-shadow-lg: 7px 7px 0 #111116;
  --comic-shadow-red: 5px 5px 0 #ff1f4b;
}
```

### 1.2. Typography & Textures
- **Headers & Title Splash**: `'Bangers', cursive`
- **SFX / Action Kanji**: `'Mochiy Pop One', sans-serif`
- **Body & Data Grid**: `'Plus Jakarta Sans', sans-serif` (weight 500/700/800) untuk keterbacaan angka tinggi.
- **Background Texture**:
  ```css
  background-color: var(--manga-paper);
  background-image: radial-gradient(circle, #2b2b36 1.2px, transparent 1.2px);
  background-size: 14px 14px;
  ```

---

## 2. Audio Engine (Web Audio API Synthesizer)
Tidak menggunakan asset file mp3/wav eksternal agar web app bebas 404 error dan loading instan. Semua audio disintesis langsung menggunakan Web Audio API:

```javascript
const AudioEngine = {
  ctx: null,
  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
    }
    if (this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  },
  playTap() {
    this.init();
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(440, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(880, this.ctx.currentTime + 0.05);
    gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.05);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.05);
  },
  playKaChing() {
    this.init();
    const now = this.ctx.currentTime;
    [987.77, 1318.51].forEach((freq, i) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, now + (i * 0.08));
      gain.gain.setValueAtTime(0.2, now + (i * 0.08));
      gain.gain.exponentialRampToValueAtTime(0.001, now + (i * 0.08) + 0.35);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now + (i * 0.08));
      osc.stop(now + (i * 0.08) + 0.35);
    });
  },
  playLimitBreak() {
    this.init();
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(150, now);
    osc.frequency.exponentialRampToValueAtTime(900, now + 0.4);
    gain.gain.setValueAtTime(0.25, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.45);
  }
};
```

---

## 3. Mathematical Logic Architecture (Algorithms)

### 3.1. Discrete Recursive Harvest Simulator
Menghitung secara presisi per batch hingga seed habis (< 1):
```javascript
function simulateHarvestLoop(initialTrees, blockYieldPerTree, seedDropRate) {
  let batches = [];
  let currentTrees = initialTrees;
  let totalTrees = 0;
  let totalBlocks = 0;
  let batchNum = 1;

  while (currentTrees >= 1) {
    const blocks = Math.floor(currentTrees * blockYieldPerTree);
    const seeds = Math.floor(currentTrees * seedDropRate);
    batches.push({
      batch: batchNum++,
      treesPlanted: currentTrees,
      blocksProduced: blocks,
      seedsDropped: seeds
    });
    totalTrees += currentTrees;
    totalBlocks += blocks;
    currentTrees = seeds; // Tanam ulang seluruh seed drop
  }

  return {
    batches,
    totalTrees,
    totalBlocks,
    remainderSeeds: currentTrees
  };
}
```

### 3.2. Discrete Recursive Break Simulator
Menghitung pemecahan balok berantai beserta sisa block drop yang dipukul kembali:
```javascript
function simulateBreakLoop(initialBlocks, seedRate = 0.25, blockDropRate = 0.1333, gemsRate = 2.2965, xpRate = 7) {
  let passes = [];
  let currentBlocks = initialBlocks;
  let totalBroken = 0;
  let totalSeeds = 0;
  let totalGems = 0;
  let totalXp = 0;
  let passNum = 1;

  while (currentBlocks >= 1) {
    const seedsOut = Math.floor(currentBlocks * seedRate);
    const blocksOut = Math.floor(currentBlocks * blockDropRate);
    const gemsOut = Math.floor(currentBlocks * gemsRate);
    const xpOut = Math.floor(currentBlocks * xpRate);

    passes.push({
      pass: passNum++,
      blocksPunched: currentBlocks,
      seedsOut,
      blocksReturned: blocksOut,
      gemsOut,
      xpOut
    });

    totalBroken += currentBlocks;
    totalSeeds += seedsOut;
    totalGems += gemsOut;
    totalXp += xpOut;
    currentBlocks = blocksOut; // Pukul ulang seluruh block drop
  }

  return {
    passes,
    totalBroken,
    totalSeeds,
    totalGems,
    totalXp,
    remainderBlocks: currentBlocks
  };
}
```

---

## 4. Layout & UI Hierarchy

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. MANGA TOP TICKER BAR (Infinite Shonen Ticker: Prices, SFX, Updates) │
├────────────────────────────────────────────────────────────────────────┤
│ 2. HERO HEADER & NET PROFIT COUNTER (Bangers Title, DL/WL Live Cuan)   │
├────────────────────────────────────────────────────────────────────────┤
│ 3. MASTER CONTROL DECK:                                                │
│    - Base Target Input: [ 6,000 ] Trees/Seeds                          │
│    - Buff Switchboard: [✓] Dreamcatcher Staff  [✓] Harvester (FP)      │
│    - Calculation Mode: (●) Perfectionist (To 0)  (○) Single-Pass Bot   │
│    - FP Strategy: [ Full FP in All Steps (Recommended: +23 DL) ▾ ]     │
├────────────────────────────────────────────────────────────────────────┤
│ 4. INTERACTIVE SPLICING TREE CANVAS:                                   │
│    ┌──────────────────────────────────────────────────────────────┐    │
│    │               [ TIER 0: SURG-E TREE (R56) ]                  │    │
│    │              Output: 17,617 Surg-E (176 DL)                  │    │
│    │                              │                               │    │
│    │       ┌──────────────────────┴──────────────────────┐        │    │
│    │  [ HOSPITAL BED (R31) ]                    [ PUZZLE BRICK ]  │    │
│    │    5,673 Seeds Made                          5,737 Seeds     │    │
│    │       ┌───────┴───────┐                     ┌───────┴──────┐ │    │
│    │    [ BED ]     [ SCREEN DOOR ]           [ OUTIE ]   [ EVIL] │    │
│    │   6,000 Seed     6,000 Seed              6,000 Seed  6,000   │    │
│    └──────────────────────────────────────────────────────────────┘    │
├────────────────────────────────────────────────────────────────────────┤
│ 5. RECURSIVE BATCH AUDIT DRAWER (Accordion: Batch 1 to 5 Details)     │
├────────────────────────────────────────────────────────────────────────┤
│ 6. FINANCIAL LEDGER & VERDICT PANEL:                                  │
│    - Capital Needed (Cash vs Sunk)                                     │
│    - Gross Revenue & Bonus (Gems + Extra Seeds)                        │
│    - Net Profit Badge (+92 DL 07 WL) with Canvas-Confetti Trigger      │
│    - Market Price Live Inputs (Editable Grid)                          │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. LocalStorage Data Schema
Semua state disimpan pada key `surg_e_calc_state_v1`:
```typescript
interface SurgECalculatorState {
  baseQuantity: number;              // default: 6000
  hasScreenDoor: boolean;            // default: true
  hasOutie: boolean;                 // default: false
  buffs: {
    dreamcatcher: boolean;           // default: true
    harvester: boolean;              // default: true
    ancestralLevel: number;          // default: 1
  };
  fpStrategy: 'all' | 'surg_only' | 'none'; // default: 'all'
  prices: {
    bedSeedRate: number;             // default: 2.0 (2/1 WL)
    screenDoorSeedRate: number;      // default: 4.0 (4/1 WL)
    outieSeedRate: number;           // default: 2.0 (2/1 WL)
    evilBrickSeedRate: number;       // default: 10.0 (10/1 WL)
    surgEBlockPrice: number;         // default: 1.0 (1/1 WL)
    fuelPackPerWlRate: number;       // default: 1.111 (200 FP = 180 WL)
  };
  calculationMode: 'recursive' | 'single'; // default: 'recursive'
}
```
