#!/usr/bin/env python3
"""
Battle of Bands - Mathematical Balance Analysis
"""

from collections import defaultdict, Counter
from itertools import combinations
import statistics

# Member Cards Database
member_cards = [
    # Bronze Technique 3
    {"rarity": "Bronze", "technique": 3, "instrument": "Vocal", "styles": ["Pop", "Rock"], "tags": ["Spotlight"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Bass", "styles": ["Pop", "Country"], "tags": ["Spotlight"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Drums", "styles": ["Jazz", "Rock"], "tags": ["Songwriting"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Bass", "styles": ["Rock", "Country"], "tags": ["Spotlight"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Sax", "styles": ["Pop", "Jazz"], "tags": ["Fame"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Drums", "styles": ["Jazz", "Pop"], "tags": ["Spotlight"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Bass", "styles": ["Pop", "Country"], "tags": ["Vibe"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Bass", "styles": ["Jazz", "Country"], "tags": ["Vibe"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Guitar", "styles": ["Country", "Pop"], "tags": ["Songwriting"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Vocal", "styles": ["Rock", "Country"], "tags": ["Fame"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Bass", "styles": ["Pop", "Rock"], "tags": ["Songwriting"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Drums", "styles": ["Jazz", "Country"], "tags": ["Fame"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Sax", "styles": ["Jazz", "Country"], "tags": ["Songwriting"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Guitar", "styles": ["Pop", "Jazz"], "tags": ["Fame"]},
    {"rarity": "Bronze", "technique": 3, "instrument": "Bass", "styles": ["Pop", "Jazz", "Rock"], "tags": []},
    {"rarity": "Bronze", "technique": 3, "instrument": "Vocal", "styles": ["Pop", "Country", "Rock"], "tags": []},
    {"rarity": "Bronze", "technique": 3, "instrument": "Keys", "styles": ["Country", "Jazz", "Rock"], "tags": []},

    # Bronze Technique 4
    {"rarity": "Bronze", "technique": 4, "instrument": "Vocal", "styles": ["Rock"], "tags": ["Vibe"]},
    {"rarity": "Bronze", "technique": 4, "instrument": "Bass", "styles": ["Jazz"], "tags": ["Vibe"]},
    {"rarity": "Bronze", "technique": 4, "instrument": "Guitar", "styles": ["Pop"], "tags": ["Spotlight"]},
    {"rarity": "Bronze", "technique": 4, "instrument": "Vocal", "styles": ["Country"], "tags": ["Spotlight"]},
    {"rarity": "Bronze", "technique": 4, "instrument": "Guitar", "styles": ["Jazz", "Country"], "tags": ["Vibe"]},
    {"rarity": "Bronze", "technique": 4, "instrument": "Bass", "styles": ["Rock", "Pop"], "tags": []},
    {"rarity": "Bronze", "technique": 4, "instrument": "Keys", "styles": ["Jazz", "Rock"], "tags": []},
    {"rarity": "Bronze", "technique": 4, "instrument": "Sax", "styles": ["Jazz", "Rock"], "tags": []},
    {"rarity": "Bronze", "technique": 4, "instrument": "Drums", "styles": ["Pop", "Rock"], "tags": []},
    {"rarity": "Bronze", "technique": 4, "instrument": "Keys", "styles": ["Pop", "Country"], "tags": []},
    {"rarity": "Bronze", "technique": 4, "instrument": "Sax", "styles": ["Country", "Rock"], "tags": []},

    # Bronze Technique 5
    {"rarity": "Bronze", "technique": 5, "instrument": "Guitar", "styles": ["Rock"], "tags": []},
    {"rarity": "Bronze", "technique": 5, "instrument": "Bass", "styles": ["Jazz"], "tags": []},
    {"rarity": "Bronze", "technique": 5, "instrument": "Vocal", "styles": ["Pop"], "tags": []},
    {"rarity": "Bronze", "technique": 5, "instrument": "Guitar", "styles": ["Country"], "tags": []},

    # Silver Technique 3
    {"rarity": "Silver", "technique": 3, "instrument": "Vocal", "styles": ["Pop"], "tags": ["Vibe", "Fame", "Spotlight"]},
    {"rarity": "Silver", "technique": 3, "instrument": "Guitar", "styles": ["Rock"], "tags": ["Songwriting", "Fame", "Spotlight"]},
    {"rarity": "Silver", "technique": 3, "instrument": "Drums", "styles": ["Pop", "Jazz"], "tags": ["Vibe", "Spotlight"]},
    {"rarity": "Silver", "technique": 3, "instrument": "Sax", "styles": ["Country", "Jazz"], "tags": ["Spotlight", "Songwriting"]},
    {"rarity": "Silver", "technique": 3, "instrument": "Bass", "styles": ["Pop", "Rock", "Jazz"], "tags": ["Vibe"]},
    {"rarity": "Silver", "technique": 3, "instrument": "Guitar", "styles": ["Pop", "Rock", "Country"], "tags": ["Spotlight"]},
    {"rarity": "Silver", "technique": 3, "instrument": "Vocal", "styles": ["Pop", "Country", "Jazz"], "tags": ["Spotlight"]},
    {"rarity": "Silver", "technique": 3, "instrument": "Sax", "styles": ["Country", "Rock", "Jazz"], "tags": ["Spotlight"]},

    # Silver Technique 4
    {"rarity": "Silver", "technique": 4, "instrument": "Vocal", "styles": ["Pop"], "tags": ["Vibe", "Spotlight"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Guitar", "styles": ["Rock"], "tags": ["Vibe", "Fame"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Sax", "styles": ["Jazz"], "tags": ["Vibe", "Spotlight"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Vocal", "styles": ["Country"], "tags": ["Vibe", "Songwriting"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Bass", "styles": ["Country", "Jazz"], "tags": ["Songwriting"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Drums", "styles": ["Rock", "Jazz"], "tags": ["Spotlight"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Vocal", "styles": ["Pop", "Rock"], "tags": ["Vibe"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Bass", "styles": ["Country", "Rock"], "tags": ["Songwriting"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Guitar", "styles": ["Pop", "Rock"], "tags": ["Fame"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Keys", "styles": ["Pop", "Jazz"], "tags": ["Songwriting"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Guitar", "styles": ["Pop", "Jazz"], "tags": ["Vibe"]},
    {"rarity": "Silver", "technique": 4, "instrument": "Bass", "styles": ["Jazz", "Country"], "tags": ["Spotlight"]},

    # Silver Technique 5
    {"rarity": "Silver", "technique": 5, "instrument": "Bass", "styles": ["Jazz"], "tags": ["Vibe"]},
    {"rarity": "Silver", "technique": 5, "instrument": "Guitar", "styles": ["Rock"], "tags": ["Spotlight"]},
    {"rarity": "Silver", "technique": 5, "instrument": "Vocal", "styles": ["Pop"], "tags": ["Vibe"]},
    {"rarity": "Silver", "technique": 5, "instrument": "Guitar", "styles": ["Country"], "tags": ["Fame"]},

    # Gold Technique 3
    {"rarity": "Gold", "technique": 3, "instrument": "Vocal", "styles": ["Jazz", "Pop"], "tags": ["Vibe", "Spotlight", "Fame"]},
    {"rarity": "Gold", "technique": 3, "instrument": "Guitar", "styles": ["Rock", "Country"], "tags": ["Vibe", "Spotlight", "Songwriting"]},
    {"rarity": "Gold", "technique": 3, "instrument": "Bass", "styles": ["Jazz", "Rock"], "tags": ["Vibe", "Songwriting", "Fame"]},
    {"rarity": "Gold", "technique": 3, "instrument": "Keys", "styles": ["Country", "Pop"], "tags": ["Songwriting", "Spotlight", "Fame"]},
    {"rarity": "Gold", "technique": 3, "instrument": "Guitar", "styles": ["Pop", "Rock", "Country"], "tags": ["Fame", "Spotlight"]},
    {"rarity": "Gold", "technique": 3, "instrument": "Bass", "styles": ["Pop", "Rock", "Jazz"], "tags": ["Vibe", "Songwriting"]},
    {"rarity": "Gold", "technique": 3, "instrument": "Vocal", "styles": ["Pop", "Jazz", "Country"], "tags": ["Vibe", "Spotlight"]},

    # Gold Technique 4
    {"rarity": "Gold", "technique": 4, "instrument": "Sax", "styles": ["Jazz", "Country"], "tags": ["Vibe", "Spotlight"]},
    {"rarity": "Gold", "technique": 4, "instrument": "Keys", "styles": ["Jazz", "Rock"], "tags": ["Vibe", "Spotlight"]},
    {"rarity": "Gold", "technique": 4, "instrument": "Vocal", "styles": ["Rock", "Country"], "tags": ["Vibe", "Spotlight"]},

    # Gold Technique 5
    {"rarity": "Gold", "technique": 5, "instrument": "Drums", "styles": ["Rock", "Pop"], "tags": ["Vibe", "Songwriting"]},
    {"rarity": "Gold", "technique": 5, "instrument": "Keys", "styles": ["Country", "Jazz"], "tags": ["Vibe"]},

    # Gold Technique 6
    {"rarity": "Gold", "technique": 6, "instrument": "Bass", "styles": ["Jazz"], "tags": ["Songwriting"]},
    {"rarity": "Gold", "technique": 6, "instrument": "Guitar", "styles": ["Rock"], "tags": ["Fame"]},
    {"rarity": "Gold", "technique": 6, "instrument": "Vocal", "styles": ["Pop"], "tags": ["Vibe"]},
    {"rarity": "Gold", "technique": 6, "instrument": "Drums", "styles": ["Country"], "tags": ["Spotlight"]},

    # Rainbow
    {"rarity": "Rainbow", "technique": 3, "instrument": "Vocal", "styles": ["Pop", "Rock", "Country"], "tags": ["Vibe", "Spotlight", "Songwriting"]},
    {"rarity": "Rainbow", "technique": 3, "instrument": "Vocal", "styles": ["Pop", "Rock"], "tags": ["Vibe", "Spotlight", "Songwriting", "Fame"]},
    {"rarity": "Rainbow", "technique": 3, "instrument": "Bass", "styles": ["Jazz", "Country"], "tags": ["Vibe", "Spotlight", "Songwriting", "Fame"]},
    {"rarity": "Rainbow", "technique": 3, "instrument": "Guitar", "styles": ["Pop", "Rock", "Country", "Jazz"], "tags": ["Vibe", "Fame"]},
    {"rarity": "Rainbow", "technique": 3, "instrument": "Keys", "styles": ["Pop", "Rock", "Country", "Jazz"], "tags": ["Songwriting", "Fame"]},
    {"rarity": "Rainbow", "technique": 5, "instrument": "Drums", "styles": ["Jazz", "Rock"], "tags": ["Vibe", "Spotlight", "Fame"]},
    {"rarity": "Rainbow", "technique": 5, "instrument": "Sax", "styles": ["Country", "Pop"], "tags": ["Vibe", "Spotlight", "Fame"]},
    {"rarity": "Rainbow", "technique": 8, "instrument": "Guitar", "styles": ["Rock"], "tags": ["Fame"]},
]

# Audience Cards
audience_cards = [
    {"name": "We want a Guitar Solo!", "requirement": ["Guitar"], "reward": 1},
    {"name": "Lay down that Bassline!", "requirement": ["Bass"], "reward": 1},
    {"name": "Sing it loud!", "requirement": ["Vocal"], "reward": 1},
    {"name": "Give us the Beat!", "requirement": ["Drums"], "reward": 2},
    {"name": "Show us those Keys!", "requirement": ["Keys"], "reward": 2},
    {"name": "Hit the Sax!", "requirement": ["Sax"], "reward": 2},
    {"name": "Steal the Spotlight!", "requirement": ["Spotlight"], "reward": 1},
    {"name": "What a masterpiece!", "requirement": ["Songwriting"], "reward": 2},
    {"name": "Pump up the energy!", "requirement": ["Vibe"], "reward": 1},
    {"name": "Show us that Star Power!", "requirement": ["Fame"], "reward": 2},
    {"name": "A true Star is born!", "requirement": ["Spotlight", "Vibe"], "reward": 2},
    {"name": "This song has soul!", "requirement": ["Songwriting", "Fame"], "reward": 3},
    {"name": "What a powerful voice!", "requirement": ["Vocal", "Vibe"], "reward": 2},
    {"name": "We love that Guitarist!", "requirement": ["Guitar", "Fame"], "reward": 2},
    {"name": "That's a clever bassline!", "requirement": ["Bass", "Songwriting"], "reward": 2},
    {"name": "Drummer's in the spotlight!", "requirement": ["Drums", "Spotlight"], "reward": 3},
    {"name": "Those Keys set the mood!", "requirement": ["Keys", "Vibe"], "reward": 3},
    {"name": "That Sax is stealing the show!", "requirement": ["Sax", "Spotlight"], "reward": 3},
]

# Special Tastes
special_tastes = [
    {"name": "3+ Vibe", "points": 1, "requirement": "tag_count", "params": {"tag": "Vibe", "min": 3}},
    {"name": "3+ Spotlight", "points": 1, "requirement": "tag_count", "params": {"tag": "Spotlight", "min": 3}},
    {"name": "1+ Bass AND 1+ Drums", "points": 1, "requirement": "instrument_and", "params": {"instruments": ["Bass", "Drums"], "min": 1}},
    {"name": "1+ Keys AND 1+ Guitar", "points": 1, "requirement": "instrument_and", "params": {"instruments": ["Keys", "Guitar"], "min": 1}},
    {"name": "1+ Vocal AND 1+ Sax", "points": 1, "requirement": "instrument_and", "params": {"instruments": ["Vocal", "Sax"], "min": 1}},
    {"name": "4 Different Instruments", "points": 1, "requirement": "diversity", "params": {"min": 4}},
    {"name": "2 Instrument A AND 2 Instrument B", "points": 1, "requirement": "pair_instruments", "params": {"count": 2}},
    {"name": "2+ Bass AND NO Guitar", "points": 1, "requirement": "exclusive", "params": {"instrument": "Bass", "min": 2, "exclude": "Guitar"}},
    {"name": "1Vocal 1Guitar 1Bass 1Drums", "points": 2, "requirement": "classic_band", "params": {"instruments": ["Vocal", "Guitar", "Bass", "Drums"]}},
    {"name": "2+ Vocal AND 2+ Spotlight", "points": 2, "requirement": "instrument_tag_and", "params": {"instrument": "Vocal", "tag": "Spotlight", "min": 2}},
    {"name": "2+ Songwriting AND NO Fame", "points": 2, "requirement": "tag_exclusive", "params": {"tag": "Songwriting", "min": 2, "exclude": "Fame"}},
    {"name": "2+ Guitar AND 2+ Vibe", "points": 2, "requirement": "instrument_tag_and", "params": {"instrument": "Guitar", "tag": "Vibe", "min": 2}},
    {"name": "2+ Fame AND NO Songwriting", "points": 2, "requirement": "tag_exclusive", "params": {"tag": "Fame", "min": 2, "exclude": "Songwriting"}},
    {"name": "All Drums OR Keys OR Sax", "points": 2, "requirement": "mono_instrument", "params": {"instruments": ["Drums", "Keys", "Sax"]}},
]

# Cities
cities = {
    "Cleveland": {"style": "Rock", "special_tastes": 0},
    "Los Angeles": {"style": "Pop", "special_tastes": 2},
    "New York City": {"style": "Jazz", "special_tastes": 2},
    "Nashville": {"style": "Country", "special_tastes": 2},
}

def analyze_card_distribution():
    """Analyze the distribution of member cards."""
    print("=" * 80)
    print("CARD DISTRIBUTION ANALYSIS")
    print("=" * 80)

    # Rarity distribution
    rarity_counts = Counter(card["rarity"] for card in member_cards)
    print(f"\n1. Rarity Distribution (Total: {len(member_cards)} unique cards):")
    for rarity in ["Bronze", "Silver", "Gold", "Rainbow"]:
        print(f"   {rarity}: {rarity_counts[rarity]} ({rarity_counts[rarity]/len(member_cards)*100:.1f}%)")

    # Technique distribution
    technique_dist = Counter(card["technique"] for card in member_cards)
    print(f"\n2. Technique Distribution:")
    for tech in sorted(technique_dist.keys()):
        print(f"   Technique {tech}: {technique_dist[tech]} cards (Avg per card: {tech})")

    avg_technique = sum(card["technique"] for card in member_cards) / len(member_cards)
    print(f"   Average Technique: {avg_technique:.2f}")

    # Instrument distribution
    instrument_counts = Counter(card["instrument"] for card in member_cards)
    print(f"\n3. Instrument Distribution:")
    for instrument in sorted(instrument_counts.keys()):
        print(f"   {instrument}: {instrument_counts[instrument]} ({instrument_counts[instrument]/len(member_cards)*100:.1f}%)")

    # Style distribution
    style_counts = defaultdict(int)
    for card in member_cards:
        for style in card["styles"]:
            style_counts[style] += 1

    print(f"\n4. Style Distribution (total mentions across all cards):")
    for style in sorted(style_counts.keys()):
        print(f"   {style}: {style_counts[style]} mentions")

    # Tag distribution
    tag_counts = defaultdict(int)
    for card in member_cards:
        for tag in card["tags"]:
            tag_counts[tag] += 1

    print(f"\n5. Tag Distribution:")
    for tag in sorted(tag_counts.keys()):
        print(f"   {tag}: {tag_counts[tag]} ({tag_counts[tag]/len(member_cards)*100:.1f}% of cards)")

    # Tags per rarity
    print(f"\n6. Average Tags per Rarity:")
    for rarity in ["Bronze", "Silver", "Gold", "Rainbow"]:
        rarity_cards = [c for c in member_cards if c["rarity"] == rarity]
        avg_tags = sum(len(c["tags"]) for c in rarity_cards) / len(rarity_cards)
        print(f"   {rarity}: {avg_tags:.2f} tags per card")

    return {
        "rarity_counts": rarity_counts,
        "technique_dist": technique_dist,
        "instrument_counts": instrument_counts,
        "style_counts": style_counts,
        "tag_counts": tag_counts,
    }

def analyze_score_ranges():
    """Analyze theoretical and realistic score ranges."""
    print("\n" + "=" * 80)
    print("SCORE RANGE ANALYSIS")
    print("=" * 80)

    # Technique Score Analysis
    print("\n1. TECHNIQUE SCORE (TS) Analysis:")
    techniques = [card["technique"] for card in member_cards]
    min_tech = min(techniques)
    max_tech = max(techniques)

    print(f"   Minimum TS (4 lowest cards): {4 * min_tech}")
    print(f"   Maximum TS (theoretical): {4 * max_tech}")

    # More realistic max: one T8, plus next highest
    techniques_sorted = sorted(techniques, reverse=True)
    realistic_max_ts = sum(techniques_sorted[:4])
    print(f"   Realistic Maximum TS (top 4 cards): {realistic_max_ts}")
    print(f"   With 3 Rehearsal tokens: +{3*2} = {realistic_max_ts + 6}")

    # Style Score Analysis
    print(f"\n2. STYLE SCORE (SS) Analysis:")
    print(f"   Minimum SS: 1 (base only)")
    print(f"   Maximum SS: 1 (base) + 4 (all match city) + 4 (max special tastes) = 9")
    print(f"   Typical SS: 1 (base) + 2-3 (partial matches) + 1-2 (special taste) = 4-6")

    # Audience Score Analysis
    print(f"\n3. AUDIENCE SCORE (AS) Analysis:")
    audience_rewards = [card["reward"] for card in audience_cards]
    print(f"   Minimum AS: 5 (base, win 0 rounds)")
    print(f"   Maximum AS: 5 (base) + {sum(sorted(audience_rewards, reverse=True)[:4])} (top 4 rewards) = {5 + sum(sorted(audience_rewards, reverse=True)[:4])}")
    print(f"   With 9 Creation tokens (3 cities × 3 actions): +6")
    print(f"   Absolute Maximum AS: {5 + sum(sorted(audience_rewards, reverse=True)[:4]) + 6}")

    # Total Score Analysis
    print(f"\n4. TOTAL SCORE Analysis:")
    scenarios = [
        ("Minimum", 12, 1, 5),
        ("Poor Performance", 15, 3, 7),
        ("Average Performance", 18, 5, 10),
        ("Good Performance", 21, 6, 12),
        ("Excellent Performance", 24, 7, 15),
        ("Outstanding Performance", 27, 8, 18),
        ("Theoretical Maximum", realistic_max_ts + 6, 9, 23),
    ]

    print(f"\n   {'Scenario':<25} {'TS':>5} {'SS':>5} {'AS':>5} {'Total':>8} {'Ratio to Min':>12}")
    print(f"   {'-'*73}")

    min_total = scenarios[0][1] * scenarios[0][2] * scenarios[0][3]
    for scenario, ts, ss, as_score in scenarios:
        total = ts * ss * as_score
        ratio = total / min_total
        print(f"   {scenario:<25} {ts:>5} {ss:>5} {as_score:>5} {total:>8} {ratio:>12.1f}x")

    return scenarios

def analyze_audience_cards():
    """Analyze audience card balance."""
    print("\n" + "=" * 80)
    print("AUDIENCE CARD BALANCE ANALYSIS")
    print("=" * 80)

    # Reward distribution
    reward_dist = Counter(card["reward"] for card in audience_cards)
    print(f"\n1. Reward Distribution:")
    for reward in sorted(reward_dist.keys()):
        print(f"   +{reward} AS: {reward_dist[reward]} cards ({reward_dist[reward]/len(audience_cards)*100:.1f}%)")

    avg_reward = sum(card["reward"] for card in audience_cards) / len(audience_cards)
    print(f"   Average Reward: {avg_reward:.2f}")

    # Requirement complexity
    print(f"\n2. Requirement Complexity:")
    single_req = [c for c in audience_cards if len(c["requirement"]) == 1]
    combo_req = [c for c in audience_cards if len(c["requirement"]) == 2]
    print(f"   Single Requirement: {len(single_req)} cards")
    print(f"   Combo Requirement (2): {len(combo_req)} cards")

    # Requirement type distribution
    print(f"\n3. Requirement Types:")
    instrument_reqs = len([c for c in audience_cards if c["requirement"][0] in ["Guitar", "Bass", "Vocal", "Drums", "Keys", "Sax"]])
    tag_reqs = len([c for c in audience_cards if c["requirement"][0] in ["Spotlight", "Songwriting", "Vibe", "Fame"]])
    combo_reqs = len([c for c in audience_cards if len(c["requirement"]) == 2])
    print(f"   Instrument Only: {instrument_reqs}")
    print(f"   Tag Only: {tag_reqs}")
    print(f"   Combo (Instrument + Tag or Tag + Tag): {combo_reqs}")

    # Value efficiency
    print(f"\n4. Value Efficiency (Reward / Requirement Complexity):")
    for card in sorted(audience_cards, key=lambda x: x["reward"] / len(x["requirement"]), reverse=True):
        efficiency = card["reward"] / len(card["requirement"])
        req_str = " + ".join(card["requirement"])
        print(f"   {efficiency:.1f}: {card['name']:<35} ({req_str}) = +{card['reward']}")

def analyze_special_tastes():
    """Analyze special taste balance."""
    print("\n" + "=" * 80)
    print("SPECIAL TASTE BALANCE ANALYSIS")
    print("=" * 80)

    # Point distribution
    point_dist = Counter(st["points"] for st in special_tastes)
    print(f"\n1. Point Distribution:")
    for points in sorted(point_dist.keys()):
        print(f"   {points} point(s): {point_dist[points]} special tastes")

    # Difficulty assessment (subjective but analytical)
    print(f"\n2. Difficulty Assessment (Estimated):")
    difficulty_ratings = {
        "3+ Vibe": "Hard",
        "3+ Spotlight": "Hard",
        "1+ Bass AND 1+ Drums": "Easy",
        "1+ Keys AND 1+ Guitar": "Easy",
        "1+ Vocal AND 1+ Sax": "Easy",
        "4 Different Instruments": "Easy",
        "2 Instrument A AND 2 Instrument B": "Medium",
        "2+ Bass AND NO Guitar": "Hard",
        "1Vocal 1Guitar 1Bass 1Drums": "Medium",
        "2+ Vocal AND 2+ Spotlight": "Very Hard",
        "2+ Songwriting AND NO Fame": "Hard",
        "2+ Guitar AND 2+ Vibe": "Hard",
        "2+ Fame AND NO Songwriting": "Hard",
        "All Drums OR Keys OR Sax": "Very Hard",
    }

    difficulty_counts = Counter(difficulty_ratings.values())
    print(f"\n   Difficulty Distribution:")
    for diff in ["Easy", "Medium", "Hard", "Very Hard"]:
        count = difficulty_counts[diff]
        print(f"   {diff}: {count} special tastes")

    print(f"\n3. Point-to-Difficulty Ratio:")
    for st in special_tastes:
        diff = difficulty_ratings[st["name"]]
        print(f"   {st['points']} pts / {diff:<10} : {st['name']}")

def analyze_city_balance():
    """Analyze city and style balance."""
    print("\n" + "=" * 80)
    print("CITY AND STYLE BALANCE ANALYSIS")
    print("=" * 80)

    # Cards matching each city style
    print(f"\n1. Cards Matching City Styles:")
    for city, info in cities.items():
        style = info["style"]
        matching_cards = [c for c in member_cards if style in c["styles"]]
        print(f"   {city} ({style}): {len(matching_cards)} cards ({len(matching_cards)/len(member_cards)*100:.1f}%)")

    # Multi-style cards advantage
    print(f"\n2. Multi-Style Card Distribution:")
    for num_styles in range(1, 5):
        cards_with_n_styles = [c for c in member_cards if len(c["styles"]) == num_styles]
        print(f"   {num_styles} style(s): {len(cards_with_n_styles)} cards")

    # Average styles per rarity
    print(f"\n3. Average Styles per Rarity:")
    for rarity in ["Bronze", "Silver", "Gold", "Rainbow"]:
        rarity_cards = [c for c in member_cards if c["rarity"] == rarity]
        avg_styles = sum(len(c["styles"]) for c in rarity_cards) / len(rarity_cards)
        print(f"   {rarity}: {avg_styles:.2f} styles per card")

def analyze_multiplicative_effects():
    """Analyze the impact of multiplicative scoring."""
    print("\n" + "=" * 80)
    print("MULTIPLICATIVE SCORING ANALYSIS")
    print("=" * 80)

    print(f"\n1. Marginal Improvement Impact:")
    base_ts, base_ss, base_as = 18, 5, 10
    base_total = base_ts * base_ss * base_as

    print(f"   Base Scenario: TS={base_ts}, SS={base_ss}, AS={base_as} → Total={base_total}")
    print(f"\n   Improving TS by 2 (e.g., 1 Rehearsal token):")
    new_total = (base_ts + 2) * base_ss * base_as
    improvement = ((new_total - base_total) / base_total) * 100
    print(f"   {base_ts+2} × {base_ss} × {base_as} = {new_total} (+{improvement:.1f}%)")

    print(f"\n   Improving SS by 2:")
    new_total = base_ts * (base_ss + 2) * base_as
    improvement = ((new_total - base_total) / base_total) * 100
    print(f"   {base_ts} × {base_ss+2} × {base_as} = {new_total} (+{improvement:.1f}%)")

    print(f"\n   Improving AS by 2:")
    new_total = base_ts * base_ss * (base_as + 2)
    improvement = ((new_total - base_total) / base_total) * 100
    print(f"   {base_ts} × {base_ss} × {base_as+2} = {new_total} (+{improvement:.1f}%)")

    print(f"\n2. Snowball Effect Analysis:")
    print(f"   A player ahead in all categories:")
    better_ts, better_ss, better_as = 22, 7, 14
    better_total = better_ts * better_ss * better_as
    gap = ((better_total - base_total) / base_total) * 100
    print(f"   TS={better_ts}, SS={better_ss}, AS={better_as} → Total={better_total}")
    print(f"   Gap: {better_total - base_total} points (+{gap:.1f}%)")

    print(f"\n   Same advantage distributed (each +4 in one dimension):")
    scenarios = [
        (base_ts + 4, base_ss, base_as),
        (base_ts, base_ss + 2, base_as),
        (base_ts, base_ss, base_as + 4),
    ]
    for i, (ts, ss, as_score) in enumerate(scenarios):
        total = ts * ss * as_score
        gap = ((total - base_total) / base_total) * 100
        print(f"   Scenario {i+1}: {ts} × {ss} × {as_score} = {total} (+{gap:.1f}%)")

def calculate_strategy_scores():
    """Calculate expected scores for different strategies."""
    print("\n" + "=" * 80)
    print("STRATEGY VIABILITY ANALYSIS")
    print("=" * 80)

    strategies = {
        "Specialist (High Technique)": {
            "description": "Focus on highest technique cards regardless of styles",
            "avg_ts": 24,
            "avg_ss": 4,
            "avg_as": 10,
        },
        "City Matcher": {
            "description": "Optimize for city style matches",
            "avg_ts": 18,
            "avg_ss": 7,
            "avg_as": 10,
        },
        "Audience Hunter": {
            "description": "Build for high-value audience cards",
            "avg_ts": 18,
            "avg_ss": 5,
            "avg_as": 14,
        },
        "Rainbow Collector": {
            "description": "Acquire rare multi-tag cards",
            "avg_ts": 20,
            "avg_ss": 6,
            "avg_as": 12,
        },
        "Balanced": {
            "description": "Moderate focus across all dimensions",
            "avg_ts": 20,
            "avg_ss": 6,
            "avg_as": 11,
        },
    }

    print(f"\n{'Strategy':<30} {'TS':>4} {'SS':>4} {'AS':>4} {'Total':>7}")
    print(f"{'-'*53}")

    for strategy, data in strategies.items():
        total = data["avg_ts"] * data["avg_ss"] * data["avg_as"]
        print(f"{strategy:<30} {data['avg_ts']:>4} {data['avg_ss']:>4} {data['avg_as']:>4} {total:>7}")
        print(f"  → {data['description']}")

def main():
    """Run all analyses."""
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "    BATTLE OF BANDS - MATHEMATICAL BALANCE ANALYSIS".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "═" * 78 + "╝")

    analyze_card_distribution()
    analyze_score_ranges()
    analyze_audience_cards()
    analyze_special_tastes()
    analyze_city_balance()
    analyze_multiplicative_effects()
    calculate_strategy_scores()

    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
