# 📋 PRODUCT REQUIREMENT DOCUMENT (PRD)
## PROJECT: SURG-E MASSING TREE & RECURSIVE REVENUE ENGINE
**Version**: 1.0.0 • **Status**: Architecture Ready • **Target Engine**: Web Standalone / Local-First

---

## 1. Executive Summary & Problem Statement
Dalam ekosistem Growtopia, **Surg-E (Surgery Entity, Rarity 56)** adalah salah satu komoditas massing paling menguntungkan sekaligus kompleks. Massing ini membutuhkan 2 cabang simetris: **Hospital Bed (R31)** dan **Puzzle Brick (R25)** yang melibatkan konversi pohon non-farmable dan pemecahan balok berulang.

### Masalah Bot Discord & Kalkulator Konvensional:
1. **Single-Pass Truncation**: Bot hanya menghitung 1 putaran panen/break. Seed drop hasil panen (~10% di H.Bed, 11% di Puzzle, 5% di Surg-E) diabaikan begitu saja dan tidak ditanam ulang sampai habis (0 seed).
2. **Ignored Block-Drop Chaining**: Saat memecah block non-farmable dengan bonus *Ancestral Tesseract*, drop block ekstra (13.33%) hanya dihitung di putaran pertama. Bot berhenti di Pass 2 dan mengabaikan Pass 3–6 serta kehilangan kalkulasi puluhan ribu Gems dan ratusan seed ekstra.
3. **Buta Biaya Bensin (Fuel Pack Tax)**: Tidak ada kalkulator yang menghitung elastisitas harga Fuel Pack (misal 200 FP / 180 WL) terhadap pertambahan hasil panen per tahap untuk memberikan rekomendasi objektif apakah layak menyalakan Harvester di tahap bahan mentah.

### Solusi Produk:
Sebuah web app interaktif bergaya **Shonen Manga / Anime Comic** (konsisten dengan universe *Science Station* dan *Display Block*) yang menyajikan visualisasi pohon splicing hierarkis, kalkulasi deret geometri rekursif hingga sisa 0, simulasi modal cash vs valuasi total, dan switchboard buff (Harvester, Dreamcatcher Staff, Ancestral).

---

## 2. Core User Personas & Use Cases
1. **The Perfectionist Masser (Primary)**:
   - Ingin mengetahui jumlah pasti bibit dan balok jika seluruh seed drop ditanam kembali dan seluruh block drop di-break berulang kali sampai habis nol.
2. **The Capital Planner**:
   - Memiliki sebagian bahan (misal 6.000 Screen Door Seed atau Outie Seed) dan ingin tahu persis berapa World Lock (WL) / Diamond Lock (DL) tunai yang wajib disiapkan di tas untuk belanja sisa bahan dan bensin.
3. **The Yield Arbitrageur**:
   - Ingin membandingkan kapan harus memecah balok vs menjual balok utuh, serta simulasi sensitivitas harga pasar secara live.

---

## 3. Product Scope & Functional Requirements

### 3.1. Splicing Tree Hierarchy (Visual Map)
Aplikasi wajib memvisualisasikan silsilah pohon secara interaktif dari Tier 0 ke Tier 2:
```
                    [ TIER 0: SURG-E TREE (R56) ]
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
[ TIER 1A: HOSPITAL BED (R31) ]           [ TIER 1B: PUZZLE BRICK (R25) ]
         │                                                 │
   ┌─────┴─────┐                                     ┌─────┴─────┐
   ▼           ▼                                     ▼           ▼
[ BED ]  [ SCREEN DOOR ]                       [ OUTIE ]   [ EVIL BRICKS ]
 (R14)        (R17)                              (R20)          (R5)
```
- **Interaktivitas Card**: Setiap node menampilkan ikon item, nama, rarity, jumlah kebutuhan bibit, perkiraan waktu panen, status ketersediaan modal (Ready / Need Buy), dan toggle inspect detail modal/breakdown.

### 3.2. Dual Recursive Engine (Until 0 Remainder)
Aplikasi wajib menyediakan switch mode: **"Single Pass (Bot Mode)"** vs **"Infinite Recursive (Perfectionist Mode)"**.

#### A. Recursive Harvest Engine (Panen Tanam Ulang Sampai 0 Seed)
- **Rumus Deret Geometri Konvergen**:
  $$\text{Total Trees Harvested} = \sum_{k=0}^{\infty} T_0 \cdot (r_{\text{seed}})^k = \frac{T_0}{1 - r_{\text{seed}}}$$
  $$\text{Total Blocks Produced} = \text{Total Trees Harvested} \times \text{Yield}_{\text{block}}$$
- **Parameter Drop per Item**:
  - **Hospital Bed (R31)**: $r_{\text{seed}} = 10.0\%$ (0.10 seed/tree). Yield: Normal 2.50, +DCS 2.575, +Harvester+DCS 2.95 blocks/tree.
  - **Puzzle Brick (R25)**: $r_{\text{seed}} = 11.0\%$ (0.11 seed/tree). Yield: Normal 2.50, +DCS 2.575, +Harvester+DCS 2.95 blocks/tree.
  - **Surg-E (R56)**: $r_{\text{seed}} = 5.0\%$ (0.05 seed/tree). Yield: Normal 2.50, +DCS 2.575, +Harvester+DCS 2.95 blocks/tree.
- **Tabel Rincian Batch**: Menampilkan akumulasi batch per batch (Batch 1, 2, 3...) hingga sisa benih < 1.

#### B. Recursive Block Break Engine (Pukul Hancur Sampai 0 Block)
- Saat memecah block Hospital Bed atau Puzzle Brick untuk mendapatkan seed Surg-E:
  - **Seed Drop Rate**: 25.0% per pukulan balok.
  - **Extra Block Drop Rate (Ancestral Tesseract Lv.1)**: 13.33%.
  - **Total Blocks Broken**:
    $$\text{Total Broken} = \frac{B_0}{1 - 0.1333} \approx B_0 \times 1.1538$$
  - **Total Seeds Generated**:
    $$\text{Total Seeds} = \text{Total Broken} \times 0.25 \approx B_0 \times 0.2885$$
- **Gems & XP Accumulator**:
  - H.Bed: ~2.2965 Gems/block, 7 XP/block.
  - P.Brick: ~1.2345 Gems/block, 6 XP/block.
  - Surg-E Harvest: ~4.148 Gems/tree, 12 XP/tree.

### 3.3. Fuel Pack (FP) & Harvester Decision Matrix
- **Input Dinamis**:
  - Rasio konsumsi: Default $2,700\text{ Pohon} = 280\text{ FP}$ ($\approx 9.6428\text{ pohon / FP}$).
  - Harga pasar FP: Default `200 FP / 180 WL` ($0.90\text{ WL / FP}$).
- **Komparasi 3 Skenario Otomatis**:
  1. *No FP*: Panen tangan biasa (+DCS only).
  2. *FP on Surg-E Only*: Harvester aktif hanya saat panen pohon Surg-E akhir (Sweet spot modal minimal).
  3. *Full FP (All Stages)*: Harvester aktif di Hospital Bed, Puzzle Brick, dan Surg-E (Maksimalisasi output mutlak).
- **Output Analisis**: Menampilkan Net Margin, Extra Hours of Breaking, dan ROI dari bensin yang dibakar.

### 3.4. Ledger Finansial & Profit Calculator
- **Market Price Inputs (Real-time editable)**:
  - Bed Seed (Default: 2/1 WL)
  - Screen Door Seed (Default: 4/1 WL)
  - Outie Block Seed (Default: 2/1 WL)
  - Evil Bricks Seed (Default: 10/1 WL)
  - Surg-E Block (Default: 1/1 WL)
  - Fuel Pack (Default: 200/180 WL)
- **Inventory Checkbox (Koleksi Bahan yang Sudah Dimiliki)**:
  - Toggle "Saya sudah punya Screen Door Seed" (mengurangi modal cash keluar).
  - Toggle "Saya buat Outie sendiri" (mengurangi belanja outie).
- **Summary Metrics**:
  - Modal Tunai Keluar (Cash Needed)
  - Valuasi Modal Penuh (Total Sunk Cost)
  - Gross Revenue (Penjualan Surg-E + Valuasi Gems + Sisa Bibit)
  - Net Profit Tunai & Net Profit Murni (dalam WL dan Diamond Locks / DL)
  - Return on Investment (ROI %).

---

## 4. Non-Functional Requirements
1. **Self-Contained Deployment**:
   - Web app harus dapat berjalan langsung sebagai single-file HTML (offline-first tanpa build tools yang rumit) ATAU Next.js static export yang kompatibel dengan GitHub Pages (`.nojekyll`).
2. **Audio-Visual Fidelity**:
   - Tema Anime/Manga Shonen Jump Comic yang konsisten: warna kertas halftone, bayangan komik pekat (`4px 4px 0 #111`), ticker bar bergerak, dan efek SFX sintetis via Web Audio API.
3. **State Persistence**:
   - Seluruh perubahan angka input (jumlah pohon, harga pasar, status checkbox inventaris) tersimpan otomatis di `localStorage`.
4. **Zero Float Bugs**:
   - Semua kalkulasi pecahan dibulatkan dengan teliti menggunakan sistem floor/round presisi game Growtopia.
