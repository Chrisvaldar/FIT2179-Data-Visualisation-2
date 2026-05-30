# Sharks in Australian Waters — Narrative & storytelling reference

Use this file to review section flow, chart titles, what each visual represents, main findings, and the prose under each figure. Text matches `index.html` unless noted.

**Data:** Australian Shark Incident Database (ASID), 1791–2022 (1,196 incidents on the national map narrative); California Shark Incident Database, 1950–2022 (Section 5).

---

## Hero

**Title:** Sharks in *Australian Waters*

**What it is:** Page masthead (not a chart).

**Main message:** The public shark story is simpler than the data. This project asks who is attacked, which species matter, and whether risk is really rising.

**Subtitle narrative:**

Over 230 years and 1,196 recorded incidents, the story of sharks and Australians is more nuanced than the headlines suggest. Who gets attacked, which sharks are truly dangerous, and does the risk actually keep growing?

---

## Section 1 — What does the shark attack history look like in Australia?

**Section story:** Establish geography and scale before drilling into species, behaviour, or demographics. Three views: every incident on the map, state-level volume vs danger, and change over time.

---

### 1.1 Every shark incident in Australia, 1791 to 2022

| | |
|---|---|
| **Chart type** | Filterable **dot map** (Mercator). One point per incident; colour = outcome (fatal / injured / uninjured). Land = sand fill, state outlines, ghosted state abbreviations at centroids. Coast annotations for dense vs sparse stretches. |
| **Data** | `dot_map.csv` · `australia.json` + `australia_states.json` |
| **Interactivity** | Dropdown: decade (1790s–2020s or all). Dropdown: outcome (all / fatal / injured / uninjured). Tooltips on dots. |
| **Spec** | `charts/section-1/dot_map.vg.json` |

**Main findings (what the chart should prove):**

- Coastal concentration is extreme; **NSW** dominates dot density (**Sydney Harbour**, northern beaches).
- Second cluster: **Gold Coast / Byron Bay** corridor (QLD).
- **WA** coast is **sparse** but long: incidents spread along a vast shoreline.
- Pre-**1900** map is thin; post-**2000** is dense (population + reporting, not only “more sharks”).
- **Fatal** dots are **not** locked to one famous beach; risk is distributed along the coast.

**Narrative (on-page lede):**

Every incident since 1791 plotted on the coast makes one thing immediately clear: **NSW** dominates in raw dot density, particularly around **Sydney Harbour** and the northern beaches. The **Gold Coast and Byron Bay corridor** form a second major cluster further north.

Filtering by decade shows the map thinning dramatically **before 1900** and becoming increasingly dense **after 2000**, reflecting both **population growth** and **improved incident reporting**. **Fatal dots** are distributed across the whole coastline rather than concentrated in any single hotspot, which suggests danger is **not confined to famous beaches**.

---

### 1.2 Volume vs danger by state

| | |
|---|---|
| **Chart type** | **Pair of choropleth maps** (side by side). **Left:** total incidents **per million people** (blue sequential). **Right:** **fatality rate** (% of incidents that were fatal, red sequential). Inline labels on large states (name + value). |
| **Data** | `state_choropleth.csv` · state TopoJSON |
| **Interactivity** | Static (comparison is the two maps themselves). Tooltips on states. |
| **Spec** | `state_choropleth_rate.vg.json` + `state_choropleth_fatal.vg.json` |

**Main findings:**

- **Volume story ≠ danger story.** NSW leads raw totals (**438 incidents**) but is mid-pack **per capita**.
- **WA** highest rate (~**71 per million**); **QLD** next (~**69 per million**).
- **VIC** lowest rate (~**10.5 per million**); colder water, less year-round beach use.
- **SA** and **QLD** share highest **fatality rate** (~**27%**) despite very different volumes.
- SA fatality linked to **white sharks** in southern waters (Neptune Islands, Eyre Peninsula).

**Narrative:**

**NSW** leads on raw volume with **438 incidents** but sits in the middle of the pack per capita. **WA** tops the rate map at around **71 incidents per million people**, followed closely by **QLD at 69 per million**, reflecting how much of both states' populations live and recreate on the coast.

**Victoria** sits at the bottom at around **10.5 per million**, consistent with colder southern waters that reduce year-round beach activity. **SA and QLD** share the highest fatality rates at around **27%**, despite having very different total incident counts. SA's elevated fatality rate is partly explained by the dominance of **white sharks** in its cooler southern waters, particularly around the **Neptune Islands** and the **Eyre Peninsula**, where great whites congregate and grow to exceptional size.

---

### 1.3 Shark incidents per decade, 1790s to 2020s

| | |
|---|---|
| **Chart type** | **Dual-metric timeline.** Default: **stacked area** by outcome (fatal / injured / uninjured) per decade. Toggle: **line + soft area** for **incidents per million Australians** (population-adjusted). Annotated peaks (2010s count, 1920s–30s rate, WW2 dip, 1937 nets). |
| **Data** | `decade_timeline.csv` |
| **Interactivity** | Dropdown: **Raw incident count** vs **Rate per million people**. Legend syncs to visible series. |
| **Spec** | `charts/section-1/decade_timeline.vg.json` |

**Main findings:**

- Raw counts **peak in the 2010s** (**231** vs **113** in the 2000s).
- Per capita, **1920s–1930s** were worse (~**14–15 per million**) than today.
- **1937** NSW shark meshing aligns with modest flattening in raw counts.
- **WW2** dip matches less beach use.
- 2010s ~**10 per million**: high, but below interwar peak → modern surge is largely **more people in the water**, not shark behaviour change.

**Narrative:**

Raw counts peak in the **2010s at 231 incidents**, more than double the **2000s figure of 113**. Switch to per capita and the picture changes considerably. The **1920s and 1930s** were actually the most dangerous decades at around **14 to 15 incidents per million Australians**, a period before beach safety infrastructure, shark nets, and aerial surveillance existed in any meaningful form.

**NSW** introduced the first shark meshing program at Sydney beaches in **1937**, which coincides with a modest flattening visible in the raw count view. The **WW2 years** show a visible dip, consistent with reduced civilian beach activity during wartime. The 2010s reach about **10 per million**, high but well below the interwar peak. The population-adjusted view makes a straightforward case that **more Australians in the water**, rather than any change in shark behaviour, accounts for most of the apparent modern surge.

---

## Section 2 — Which shark should you actually fear?

**Section story:** Separate **which species bite often** from **which species kill**, then whether **size** explains volume.

---

### 2.1 Which shark should you actually fear?

| | |
|---|---|
| **Chart type** | **Sankey diagram** (Vega). Left: species (or species group). Right: outcome (fatal / injured / uninjured). Band width = incident count. |
| **Data** | `species_sankey.csv` |
| **Interactivity** | **Click a species** to filter flows; reset control. Hover tooltips (count + share). |
| **Spec** | `charts/section-2/species_sankey.vg.json` |

**Main findings:**

- **White, tiger, bull** account for nearly all **~250 fatalities** (white **91**, tiger **86**, bull **63**).
- Those three are large, predatory, and in the same shallow coastal habitat as swimmers.
- **Wobbegong:** **201 incidents, zero deaths**; almost all flows end in **injured**.
- Thick band ≠ deadly species (sets up chart 2.2).

**Narrative:**

**White, tiger, and bull sharks** account for nearly all **250 recorded fatalities**. White sharks lead at **91 deaths**, tiger sharks at **86**, bull sharks at **63**. These three species share a key trait: they are **large, genuinely predatory**, and found in the same coastal shallows where Australians swim.

The **wobbegong** band is thick on the left but terminates almost entirely in the injured column. **201 incidents, zero deaths**. Wobbegongs are ambush predators that sit camouflaged on reef and sandy bottoms; they bite when stepped on or handled and then let go. A wide band here does **not** mean a large shark. But are the sharks involved in more incidents generally bigger?

---

### 2.2 Most incidents does not mean the biggest shark

| | |
|---|---|
| **Chart type** | **Custom icon chart** (Vega). Shared shark silhouette per row; **horizontal width = median recorded length (m)**. Rows = six species groups; labels for median length and incident count. |
| **Data** | `species_size_icons.csv` |
| **Interactivity** | Static. Tooltips on rows. |
| **Spec** | `charts/section-2/species_size_icons.vg.json` |

**Main findings:**

- **Wobbegong:** 3rd in volume (**201** bites), **smallest** median (**1.2 m**).
- **White** and **tiger:** high volume **and** **3.0 m** median; align with sankey fatality story.
- **Takeaway:** Incident count alone is a poor proxy for how large or lethal the shark was.

**Narrative:**

**No.** Wobbegong ranks third for incident volume at **201 bites** yet its median recorded length is just **1.2 m**, the smallest of the six groups. These are bottom-dwelling ambush fish, not open-water predators. High incident count and large body size simply do not go hand in hand.

The species driving the death toll in the sankey are a different story. **White sharks** (**361 incidents**, **3.0 m** median) and **tiger sharks** (**229**, **3.0 m**) are among the largest sharks in the database and among the deadliest. For the sharks that actually kill, size and danger align. Volume alone is a poor guide to how big the animal was.

---

## Section 3 — Risk depends on what you are doing

**Section story:** Risk is behavioural and temporal, not only geographic. Activity drives fatality rate; time-of-day challenges the “dawn patrol” myth.

---

### 3.1 Activity risk, volume vs fatality rate

| | |
|---|---|
| **Chart type** | **Butterfly / paired lollipop** (horizontal). **Left arm:** incident **count** (extends left). **Right arm:** **fatality rate %** (extends right). Shared y-axis = cleaned activity type. |
| **Data** | `activity_risk.csv` |
| **Interactivity** | Static. Labels on both arms. |
| **Spec** | `charts/section-3/activity_risk.vg.json` |

**Main findings:**

- **Swimming:** most incidents (**451**) and highest fatality rate (**34.6%** vs **22.6%** overall); submerged profile like prey.
- **Surfing/boarding:** **284** incidents but only **9.5%** fatal; bites often investigatory.
- **Fishing + boating:** **70** incidents, **0** deaths; victim rarely fully in water.

**Narrative:**

**Swimming** sits at the far right on both arms: **451 incidents** and a **34.6% fatality rate**. This is higher than the overall fatality rate of **22.6%**, and the gap is partly explained by **body position**. A swimmer is mostly submerged, moving slowly, and presents a profile similar to a seal from below.

**Surfing and boarding** produce **284 incidents** but only a **9.5% fatality rate**. Surfers are moving faster, partially above the surface, and shark bites in this context tend to be **investigatory rather than predatory**: the shark bites once and retreats, which is consistent with the low death rate. **Fishing and boating** together account for **70 incidents and zero deaths**, likely because the victim is never fully in the water.

---

### 3.2 Peak hour is 4pm, not dawn

| | |
|---|---|
| **Chart type** | **Radial / 24-hour clock**. Outer ring: total incidents by hour. Inner ring: fatal incidents by hour. Clock layout (midnight top). |
| **Data** | `radial_time.csv` |
| **Interactivity** | Dropdown: total + fatal / total only / fatal only. Annotations at **4 pm** and **11 am** peaks. |
| **Spec** | `charts/section-3/radial_time_clock.vg.json` |

**Main findings:**

- **Midnight–5 am:** only **11** incidents; dial nearly empty.
- **Peak: 4 pm** (**55** total, **17** fatal); secondary **11 am** bump.
- Fatal ring **tracks** total ring (no hour where survival odds collapse).
- Story: **crowded beaches + afternoon glare**, not classic dawn/dusk framing.

**Narrative:**

The dial is nearly empty between **midnight and 5 am**, just **11 incidents** across those five hours. Incidents build through the morning and peak sharply at **4 pm with 55 total and 17 fatal**. There is a secondary spike around **11 am**.

The **4 pm peak** coincides with peak beach attendance during Australian summers and with the **low afternoon sun angle** that creates glare and reduces underwater visibility, making it harder for both swimmers to see approaching sharks and potentially harder for sharks to identify what they are approaching. The fatal inner ring tracks the outer ring without spiking at any specific hour, meaning **the time of day does not dramatically change your odds of surviving a bite if one occurs**.

---

## Section 4 — Who gets attacked

**Section story:** Demographics. Gender is exposure-heavy; age peaks for both fatal and survived outcomes in mid-teens.

---

### 4.1 Nine in ten victims are male

| | |
|---|---|
| **Chart type** | **Isotype / pictogram** (unit chart). Icons = 10 incidents each; male vs female silhouettes; fill = outcome. Summary stats for count and fatality rate by gender. |
| **Data** | `gender_isotype.csv` |
| **Interactivity** | Static. Page legend: icon scale (1 icon = 10 incidents). |
| **Spec** | `charts/section-4/gender_isotype.vg.json` |

**Main findings:**

- **~90%** of victims male (**1,060 / 1,177**).
- Male fatality **21.9%** vs female **13.7%**; gap partly **exposure** (surf, spearfishing, diving, boards).
- Fatality gap smaller than volume gap but real (activity mix, not biology alone).

**Narrative:**

**Males** account for **1,060 of 1,177 victims**, roughly **90%**. The male fatality rate sits at **21.9%** compared to **13.7%** for females. The volume gap is largely an **exposure gap**: surveys of Australian beach attendance and water activity consistently show men spending more time in the surf, swimming further from shore, and dominating activities like **spearfishing, diving, and board sports** that involve prolonged submersion in deeper water.

The fatality rate gap is smaller but real, and it likely reflects the same activity skew. A man spearfishing in 10 metres of water and a woman swimming inside the flags at **Bondi** face very different risk profiles, and the aggregate numbers reflect that difference.

---

### 4.2 Fatal and survived both peak in the mid-teens

| | |
|---|---|
| **Chart type** | **Mirrored density ridge** (kernel density). **Top half:** fatal incidents by victim age. **Bottom half:** survived (injured + uninjured). Age only where recorded (**697 / 1,203**). |
| **Data** | `age_records.csv` |
| **Interactivity** | Static. Annotations at fatal peak (**16**) and survived peak (**17**). |
| **Spec** | `charts/section-4/age_mirror_ridge.vg.json` |

**Main findings:**

- Both outcomes peak **10–25**; fatal peak age **16** (**14** incidents), survived peak **17** (**27**).
- Fatal curve wider into **20s–30s** but still young-adult skew.
- Survived outnumber fatal at almost every age under **30** (volume, not a separate “old victim” story).

**Narrative:**

Where age is recorded (**697 of 1,203** incidents), the two curves tell separate stories. Among **fatal** attacks, the sharpest concentration sits at age **16** (14 incidents), with most deaths still falling between **10 and 25**. The fatal ridge is wider than the survived one, spreading further into the **20s and 30s**, but it never leaves the young-adult range.

Among those who **survived**, the single-year peak is age **17** (27 incidents), with the same broad **10–25** cluster. Both outcomes skew young because teenagers and young adults spend the most time in the water. The difference is volume and spread, not a wholesale shift to middle age: survived incidents outnumber fatal ones at almost every age under 30.

---

## Section 5 — How does Australia compare with California?

**Section story:** Peer comparison at **state scale** (NSW vs California), same era (1950+), white-shark-focused CA data. Geography vs culture; rates vs raw counts.

---

### 5.1 Two leading states, two coastal geographies

| | |
|---|---|
| **Chart type** | **Side-by-side dot maps** (NSW left, California right). Same outcome encoding as Section 1. Coast annotations (Sydney/Central Coast, Byron; CA Red Triangle / San Diego). |
| **Data** | `nsw_dot_map.csv` · `ca_dot_map.csv` · state + California TopoJSON |
| **Interactivity** | **Shared HTML filters** (page-level): decade (1950s–2020s), outcome. Tooltips on dots. |
| **Spec** | `nsw_dot_map.vg.json` + `ca_dot_map.vg.json` |

**Main findings:**

- **NSW:** **286** incidents since 1950; **two clusters** (Sydney/Central Coast + Byron).
- **California:** **202** white-shark incidents; **~70%** in San Diego–Mendocino corridor.
- Both surf-heavy (**51%** NSW vs **43%** CA board-related); difference is **geographic spread** (long NSW coast vs tight CA triangle).

**Narrative:**

At state scale the comparison finally balances. **New South Wales** leads Australia with **286 incidents since 1950**, spread between a **Sydney and Central Coast cluster** and a second band around **Byron Bay**. California records **202 white-shark incidents** in the same period, but **roughly seven in ten** fall inside the surf corridor from San Diego to Mendocino.

Both states are board-heavy surf cultures: **51%** of NSW incidents involve surfing or boarding, against **43%** in California. The difference is geography, not appetite for risk: NSW still spans hundreds of kilometres of coast, while California packs most of its dots into one visible triangle. The national picture remains in Section 1; this is the state-level peer comparison.

---

### 5.2 Injury outcomes per million people (with raw counts available)

| | |
|---|---|
| **Chart type** | **Grouped bar chart**. X = outcome (fatal / injured / uninjured). Bars = **California** then **NSW** within each group. Default y = **rate per million** (2021 population); toggle **raw counts**. |
| **Data** | `outcome_comparison.csv` |
| **Interactivity** | Dropdown: rate per million vs raw count. Region legend (CA navy, NSW sand). |
| **Spec** | `charts/section-5/outcome_comparison.vg.json` |

**Main findings:**

- **Injured rate:** NSW **22.8/million** vs CA **2.75/million** (largest gap).
- **Fatal rate:** closer (**2.45** NSW vs **0.38** CA per million).
- Raw counts: NSW leads injured (**186** vs **108**); uninjured nearly tied (**80** vs **79**).
- **~7%** of all incidents fatal in both regions.

**Narrative:**

Bars default to **incidents per million people** (2021 populations) so the two states compare on a level footing. Read each cluster left to right: **California** then **NSW**. Injured encounters dominate in NSW at **22.8 per million** against California's **2.75**; fatalities stay closer (**0.38** vs **2.45**).

Switch to **raw incident count** and the picture softens but the pattern holds: NSW leads on injured (**186** vs **108**), while uninjured totals are almost tied (**80** vs **79**). The share of all incidents that ended in death stays near **7%** in both places.

---

## Storytelling checklist (quick reference)

| # | Title | One-line takeaway |
|---|--------|-------------------|
| 1.1 | Every shark incident in Australia, 1791 to 2022 | NSW coast dominates; fatals are widespread, not one beach. |
| 1.2 | Volume vs danger by state | Most incidents ≠ most dangerous state; SA/QLD fatality rate stands out. |
| 1.3 | Shark incidents per decade, 1790s to 2020s | Rising counts; per capita, today is not the worst era. |
| 2.1 | Which shark should you actually fear? | Three species kill; wobbegong bites constantly but does not kill. |
| 2.2 | Most incidents does not mean the biggest shark | High bite count can be a small ambush species. |
| 3.1 | Activity risk, volume vs fatality rate | Swimming is deadliest; surfing common but rarely fatal. |
| 3.2 | Peak hour is 4pm, not dawn | Afternoon beach crowd, not horror-film timing. |
| 4.1 | Nine in ten victims are male | Exposure explains most of the gender gap. |
| 4.2 | Fatal and survived both peak in the mid-teens | Youth in the water drives both curves. |
| 5.1 | Two leading states, two coastal geographies | Same surf culture, different coastal geometry. |
| 5.2 | Injury outcomes per million people | NSW injured rate far higher; fatality share similar. |

---

## Data sources

- [Australian Shark Incident Database (ASID)](https://github.com/cjabradshaw/AustralianSharkIncidentDatabase), 1791–2022
- [California Shark Incident Database](https://data.ca.gov/dataset/shark-incident-database-california), 1950–2022

FIT2179 Data Visualisation 2 · Semester 1, 2026
