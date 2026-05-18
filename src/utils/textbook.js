const TEXTBOOK = {
  name: '人教版化学',
  chapters: [
  {
    "id": "ch1",
    "name": "第一章 物质及其变化",
    "sections": [
      {
        "id": "ch1_elec",
        "name": "电解质与离子反应",
        "substances": [
          {
            "id": "ch1_hcl",
            "name": "HCl 盐酸",
            "icon": "🧪",
            "note": "强酸、强电解质",
            "reactions": [
              {
                "id": "ch1_hcl1",
                "name": "HCl 电离",
                "equation": "HCl = H⁺ + Cl⁻",
                "category": "电离",
                "note": "强电解质完全电离"
              },
              {
                "id": "ch1_hcl2",
                "name": "HCl + NaOH",
                "equation": "HCl + NaOH = NaCl + H₂O",
                "category": "中和",
                "note": " 💯 H⁺ + OH⁻ = H₂O"
              },
              {
                "id": "ch1_hcl3",
                "name": "HCl + Na₂CO₃",
                "equation": "2HCl + Na₂CO₃ = 2NaCl + H₂O + CO₂↑",
                "category": "与盐",
                "phenomenon": "产生气泡",
                "note": "CO₃²⁻ + 2H⁺ = H₂O + CO₂↑"
              }
            ]
          },
          {
            "id": "ch1_naoh",
            "name": "NaOH 氢氧化钠",
            "icon": "🧴",
            "note": "强碱、强电解质",
            "reactions": [
              {
                "id": "ch1_naoh1",
                "name": "NaOH 电离",
                "equation": "NaOH = Na⁺ + OH⁻",
                "category": "电离",
                "note": "强电解质完全电离"
              },
              {
                "id": "ch1_naoh2",
                "name": "NaOH + HCl",
                "equation": "NaOH + HCl = NaCl + H₂O",
                "category": "中和",
                "note": "中和反应"
              },
              {
                "id": "ch1_naoh3",
                "name": "NaOH + CuSO₄",
                "equation": "2NaOH + CuSO₄ = Cu(OH)₂↓ + Na₂SO₄",
                "category": "复分解",
                "phenomenon": "蓝色沉淀",
                "note": "复分解反应条件：有沉淀"
              }
            ]
          },
          {
            "id": "ch1_na2so4",
            "name": "Na₂SO₄ 硫酸钠",
            "icon": "🧂",
            "note": "盐、强电解质",
            "reactions": [
              {
                "id": "ch1_ns1",
                "name": "Na₂SO₄ 电离",
                "equation": "Na₂SO₄ = 2Na⁺ + SO₄²⁻",
                "category": "电离",
                "note": "强电解质完全电离"
              }
            ]
          },
          {
            "id": "ch1_feoh3",
            "name": "Fe(OH)₃胶体",
            "icon": "🧫",
            "note": "胶体制备",
            "reactions": [
              {
                "id": "ch1_col1",
                "name": "Fe(OH)₃胶体制备",
                "equation": "FeCl₃ + 3H₂O =(加热) Fe(OH)₃(胶体) + 3HCl",
                "category": "水解",
                "phenomenon": "溶液呈红褐色",
                "note": " 💯 丁达尔效应！不能写↓"
              }
            ]
          }
        ]
      }
    ]
  }
],
};

function flattenReactions(textbook) {
  const all = [];
  textbook.chapters.forEach(ch => {
    ch.sections.forEach(sec => {
      sec.substances.forEach(sub => {
        sub.reactions.forEach(r => {
          all.push({
            ...r,
            substanceId: sub.id,
            substanceName: sub.name,
            substanceIcon: sub.icon,
            substanceNote: sub.note,
            sectionId: sec.id,
            sectionName: sec.name,
            chapterId: ch.id,
            chapterName: ch.name,
          });
        });
      });
    });
  });
  return all;
}

const ALL_REACTIONS = flattenReactions(TEXTBOOK);
export { TEXTBOOK, ALL_REACTIONS };
