// =====================================================================
// DROID-PET DISCORD SCRAPER (PASTE DI CONSOLE F12 PADA TAB DISCORD)
// =====================================================================
(() => {
  const results = {
    harvest: {},
    break: {}
  };

  // Ambil semua container embed di chat Discord yang sedang tampil
  const embeds = document.querySelectorAll('[class*="embedWrapper"], [class*="grid-"]');
  console.log(`Menemukan ${embeds.length} elemen embed...`);

  embeds.forEach(embed => {
    const text = embed.innerText || "";
    
    // Deteksi jika ini embed Harvest dari Droid-Pet
    if (text.includes("Drops from harvesting")) {
      const titleMatch = text.match(/harvesting\s+([\d,]+)\s+(.+?)\s+Tree/i);
      const gemMatch = text.match(/Gem drops:\s*([\d,]+)/i);
      const blockMatch = text.match(/Block drops:\s*([\d,]+)/i);
      const seedMatch = text.match(/Seed Drops:\s*([\d,]+)/i);
      const xpMatch = text.match(/XP Earned:\s*([\d,]+)/i);

      if (titleMatch) {
        const treeCount = parseInt(titleMatch[1].replace(/,/g, ""), 10);
        const itemName = titleMatch[2].trim();
        
        results.harvest[itemName] = {
          tree_count: treeCount,
          block_drops: blockMatch ? parseInt(blockMatch[1].replace(/,/g, ""), 10) : 0,
          seed_drops: seedMatch ? parseInt(seedMatch[1].replace(/,/g, ""), 10) : 0,
          gem_drops: gemMatch ? parseInt(gemMatch[1].replace(/,/g, ""), 10) : 0,
          xp_earned: xpMatch ? parseInt(xpMatch[1].replace(/,/g, ""), 10) : 0
        };
      }
    }

    // Deteksi jika ini embed Break dari Droid-Pet
    if (text.includes("Breaking") && text.includes("Cactus") || text.includes("Breaking")) {
      const titleMatch = text.match(/Breaking\s+([\d,]+)\s+([^.\n]+)/i);
      const gemMatch = text.match(/Gem drops:\s*([\d,]+)/i);
      const blockMatch = text.match(/Block drops:\s*([\d,]+)/i);
      const seedMatch = text.match(/Seed [Dd]rops:\s*([\d,]+)/i);
      const extraSeedMatch = text.match(/Total with extra seeds\s*≈?\s*([\d,]+)/i);
      const xpMatch = text.match(/XP Earned:\s*([\d,]+)/i);

      if (titleMatch) {
        const blockCount = parseInt(titleMatch[1].replace(/,/g, ""), 10);
        const itemName = titleMatch[2].replace(/[.]/g, "").trim();

        results.break[itemName] = {
          block_count: blockCount,
          extra_block_drops: blockMatch ? parseInt(blockMatch[1].replace(/,/g, ""), 10) : 0,
          seed_drops: seedMatch ? parseInt(seedMatch[1].replace(/,/g, ""), 10) : 0,
          total_seed_drops: extraSeedMatch ? parseInt(extraSeedMatch[1].replace(/,/g, ""), 10) : (seedMatch ? parseInt(seedMatch[1].replace(/,/g, ""), 10) : 0),
          gem_drops: gemMatch ? parseInt(gemMatch[1].replace(/,/g, ""), 10) : 0,
          xp_earned: xpMatch ? parseInt(xpMatch[1].replace(/,/g, ""), 10) : 0
        };
      }
    }
  });

  console.log("=== HASIL SCRAPING DROID-PET ===");
  console.log(results);

  // Otomatis download file JSON ke folder Downloads laptop lu
  const blob = new Blob([JSON.stringify(results, null, 2)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "droid_pet_harvest_break_data.json";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);

  alert(`BERHASIL! Data ${Object.keys(results.harvest).length} Harvest & ${Object.keys(results.break).length} Break telah di-download sebagai droid_pet_harvest_break_data.json!`);
})();
