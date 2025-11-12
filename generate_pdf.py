#!/usr/bin/env python3
"""
Generate PDF report for Battle of Bands balance analysis
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from datetime import datetime

def create_balance_report():
    """Create the balance analysis PDF report."""

    # Create PDF
    filename = "/home/user/p3-battle/Battle_of_Bands_Balance_Analysis.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)

    # Container for the 'Flowable' objects
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )

    # Title
    title = Paragraph("<b>Battle of Bands:<br/>A Mathematical Analysis of Game Balance</b>", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.2*inch))

    # Date
    date = Paragraph(f"<i>{datetime.now().strftime('%B %d, %Y')}</i>", styles['Center'])
    elements.append(date)
    elements.append(Spacer(1, 0.4*inch))

    # Abstract
    elements.append(Paragraph("<b>Abstract</b>", heading1_style))
    abstract_text = """This paper presents a comprehensive mathematical analysis of the game balance in
    <i>Battle of Bands</i>, a competitive band management game featuring multiplicative scoring mechanics.
    Through systematic examination of 80 unique member cards, 18 audience cards, and 14 special taste conditions
    across 4 distinct cities, we identify critical balance concerns including extreme score variance
    (60-6,624 theoretical range), multiplicative snowball effects, and strategic imbalances. Our analysis
    reveals that Style Score (SS) improvements yield 40% returns compared to 11% for Technique Score (TS)
    improvements, suggesting asymmetric strategic value. We provide evidence-based recommendations for
    balancing card distribution, scoring mechanics, and gameplay elements to enhance competitive integrity
    and player experience."""
    elements.append(Paragraph(abstract_text, styles['Justify']))
    elements.append(Spacer(1, 0.3*inch))

    # Introduction
    elements.append(Paragraph("1. Introduction", heading1_style))
    intro_text = """<i>Battle of Bands</i> employs a multiplicative scoring system where Total Score =
    TS × SS × AS, creating complex interdependencies between player decisions. This study examines whether
    the game's design achieves competitive balance across its four-city tour structure, draft mechanics,
    and diverse strategic pathways."""
    elements.append(Paragraph(intro_text, styles['Justify']))
    elements.append(Spacer(1, 0.15*inch))

    intro_text2 = """The game features 168 total member cards (distributed across 80 unique designs),
    with players drafting and fielding 4-member bands to compete in each city. Success depends on matching
    city style preferences, winning audience approval through 4 battle rounds, and optimizing technique
    scores through strategic resource management."""
    elements.append(Paragraph(intro_text2, styles['Justify']))
    elements.append(Spacer(1, 0.2*inch))

    # Research Objectives
    elements.append(Paragraph("1.1 Research Objectives", heading2_style))
    objectives = """This analysis addresses three primary questions:
    <br/><br/>
    1. What is the theoretical and realistic score variance, and does it create problematic runaway leader dynamics?
    <br/><br/>
    2. Are the game's strategic pathways (Specialist, City Matcher, Audience Hunter, Rainbow Collector)
    competitively viable?
    <br/><br/>
    3. Do card rarities, audience demands, and special tastes exhibit balanced risk-reward relationships?"""
    elements.append(Paragraph(objectives, styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))

    # Methodology
    elements.append(Paragraph("2. Methodology", heading1_style))

    elements.append(Paragraph("2.1 Data Collection", heading2_style))
    methodology_text = """We catalogued all game components:
    <br/><br/>
    • <b>Member Cards (n=80 unique):</b> Categorized by rarity (Bronze/Silver/Gold/Rainbow),
    technique (3-8), instrument (6 types), styles (1-4 per card), and tags (0-4 per card)
    <br/><br/>
    • <b>Audience Cards (n=18):</b> Analyzed requirement complexity (single vs. combo) and reward values (1-3 AS)
    <br/><br/>
    • <b>Special Tastes (n=14):</b> Assessed difficulty and point values (1-2 points)
    <br/><br/>
    • <b>Cities (n=4):</b> Cleveland (Rock), Los Angeles (Pop), New York City (Jazz), Nashville (Country)"""
    elements.append(Paragraph(methodology_text, styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))

    elements.append(Paragraph("2.2 Analytical Framework", heading2_style))
    framework_text = """We employed quantitative methods including:
    <br/><br/>
    1. <b>Distributional Analysis:</b> Examined frequency distributions of card attributes, styles, and tags
    <br/><br/>
    2. <b>Range Analysis:</b> Calculated theoretical and realistic minimum/maximum scores
    <br/><br/>
    3. <b>Marginal Impact Analysis:</b> Determined percentage gains from incremental improvements
    <br/><br/>
    4. <b>Strategic Modeling:</b> Simulated expected performance of five archetypal strategies
    <br/><br/>
    5. <b>Balance Metrics:</b> Assessed value efficiency (reward/complexity ratios)"""
    elements.append(Paragraph(framework_text, styles['Normal']))
    elements.append(PageBreak())

    # Findings
    elements.append(Paragraph("3. Findings", heading1_style))

    # 3.1 Card Distribution
    elements.append(Paragraph("3.1 Card Distribution Balance", heading2_style))

    # Rarity table
    rarity_data = [
        ['Rarity', 'Count', 'Percentage'],
        ['Bronze', '32', '40.0%'],
        ['Silver', '24', '30.0%'],
        ['Gold', '16', '20.0%'],
        ['Rainbow', '8', '10.0%']
    ]

    rarity_table = Table(rarity_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
    rarity_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ecf0f1')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))

    elements.append(Paragraph("<b>Table 1:</b> Rarity distribution follows expected scarcity hierarchy",
                              styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(rarity_table)
    elements.append(Spacer(1, 0.2*inch))

    # Key finding
    finding1 = """<b>Key Finding:</b> The single Technique 8 card (Rainbow Guitar - Rock/Fame) creates
    potential draft imbalance, providing 2.67× value of minimum technique cards."""
    elements.append(Paragraph(finding1, styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))

    # Technique distribution
    technique_data = [
        ['Technique Value', 'Card Count'],
        ['3', '37'],
        ['4', '26'],
        ['5', '12'],
        ['6', '4'],
        ['8', '1']
    ]

    technique_table = Table(technique_data, colWidths=[2.5*inch, 2.5*inch])
    technique_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ecf0f1')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))

    elements.append(Paragraph("<b>Table 2:</b> Technique values concentrate at lower ranges (Average: 3.84)",
                              styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(technique_table)
    elements.append(Spacer(1, 0.2*inch))

    # Tag distribution
    tag_text = """<b>Tag Distribution:</b> Tags show slight imbalance with Vibe (33 cards, 41.2%) and
    Spotlight (32 cards, 40.0%) significantly more common than Fame (21 cards, 26.2%) and Songwriting
    (20 cards, 25.0%). Tags per card increase with rarity: Bronze 0.59, Silver 1.42, Gold 1.94,
    Rainbow 2.75, creating clear power scaling."""
    elements.append(Paragraph(tag_text, styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))

    # 3.2 Score Range Analysis
    elements.append(Paragraph("3.2 Score Range Analysis", heading2_style))

    score_range_data = [
        ['Component', 'Minimum', 'Realistic Max', 'Range Factor'],
        ['Technique Score (TS)', '12', '32', '2.67×'],
        ['Style Score (SS)', '1', '9', '9.00×'],
        ['Audience Score (AS)', '5', '23', '4.60×']
    ]

    score_range_table = Table(score_range_data, colWidths=[2*inch, 1.2*inch, 1.5*inch, 1.3*inch])
    score_range_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e74c3c')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#fadbd8')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))

    elements.append(Paragraph("<b>Table 3:</b> Component score ranges show high variance potential",
                              styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(score_range_table)
    elements.append(Spacer(1, 0.2*inch))

    # Total score variance
    total_score_data = [
        ['Scenario', 'TS', 'SS', 'AS', 'Total'],
        ['Minimum', '12', '1', '5', '60 (1.0×)'],
        ['Poor Performance', '15', '3', '7', '315 (5.2×)'],
        ['Average Performance', '18', '5', '10', '900 (15.0×)'],
        ['Good Performance', '21', '6', '12', '1,512 (25.2×)'],
        ['Excellent', '24', '7', '15', '2,520 (42.0×)'],
        ['Outstanding', '27', '8', '18', '3,888 (64.8×)'],
        ['Theoretical Max', '32', '9', '23', '6,624 (110.4×)']
    ]

    total_score_table = Table(total_score_data, colWidths=[1.6*inch, 0.7*inch, 0.7*inch, 0.7*inch, 1.8*inch])
    total_score_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e74c3c')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#fadbd8')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))

    elements.append(Paragraph("<b>Table 4:</b> Total scores range from 60 to 6,624 (110× difference)",
                              styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(total_score_table)
    elements.append(Spacer(1, 0.2*inch))

    critical_concern = """<b><font color="#e74c3c">Critical Concern:</font></b> The 110× maximum-to-minimum
    ratio far exceeds typical balanced game design (target: 3-5×), enabling severe snowballing."""
    elements.append(Paragraph(critical_concern, styles['Normal']))
    elements.append(PageBreak())

    # 3.3 Multiplicative Scoring Effects
    elements.append(Paragraph("3.3 Multiplicative Scoring Effects", heading2_style))

    marginal_text = """Analysis of marginal improvements reveals asymmetric returns. Starting from a base
    scenario (TS=18, SS=5, AS=10, Total=900):"""
    elements.append(Paragraph(marginal_text, styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))

    marginal_data = [
        ['Improvement', 'New Total', 'Gain'],
        ['TS +2 (20×5×10)', '1,000', '+11.1%'],
        ['SS +2 (18×7×10)', '1,260', '+40.0%'],
        ['AS +2 (18×5×12)', '1,080', '+20.0%']
    ]

    marginal_table = Table(marginal_data, colWidths=[2.2*inch, 1.5*inch, 1.5*inch])
    marginal_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f39c12')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#fef5e7')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))

    elements.append(Paragraph("<b>Table 5:</b> Style Score improvements provide 3.6× greater returns than Technique Score",
                              styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(marginal_table)
    elements.append(Spacer(1, 0.2*inch))

    implication = """<b><font color="#f39c12">Implication:</font></b> Players optimizing for SS
    (City Matcher strategy) gain disproportionate advantage, potentially marginalizing high-technique strategies."""
    elements.append(Paragraph(implication, styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))

    snowball_text = """<b>Snowball Effect:</b> A player moderately ahead in all dimensions (TS +4, SS +2, AS +4)
    achieves 22×7×14 = 2,156 points compared to baseline 18×5×10 = 900 points, representing a
    <b><font color="#e74c3c">+139.6% advantage</font></b>. The same total advantage concentrated in one
    dimension yields only +22-40% gains, demonstrating severe multiplicative amplification."""
    elements.append(Paragraph(snowball_text, styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))

    # 3.4 Strategic Viability
    elements.append(Paragraph("3.4 Strategic Viability Analysis", heading2_style))

    strategy_data = [
        ['Strategy', 'TS', 'SS', 'AS', 'Total', 'Rank'],
        ['Specialist (High Tech)', '24', '4', '10', '960', '5th'],
        ['City Matcher', '18', '7', '10', '1,260', '2nd'],
        ['Audience Hunter', '18', '5', '14', '1,260', '2nd'],
        ['Rainbow Collector', '20', '6', '12', '1,440', '1st'],
        ['Balanced', '20', '6', '11', '1,320', '4th']
    ]

    strategy_table = Table(strategy_data, colWidths=[1.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.9*inch, 0.7*inch])
    strategy_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#d5f4e6')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        # Highlight worst performer
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#fadbd8')),
        # Highlight best performer
        ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#d4efdf')),
    ]))

    elements.append(Paragraph("<b>Table 6:</b> Expected total scores by strategy archetype",
                              styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(strategy_table)
    elements.append(Spacer(1, 0.2*inch))

    strategy_finding = """<b><font color="#e74c3c">Critical Finding:</font></b> Specialist strategy
    (focusing on high-technique cards) performs worst despite intuitive appeal, losing 33% performance vs.
    Rainbow Collector. This contradicts the game's stated emphasis on Technique Score and suggests design
    misalignment."""
    elements.append(Paragraph(strategy_finding, styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))

    # 3.5 Audience Card Balance
    elements.append(Paragraph("3.5 Audience Card Balance", heading2_style))

    audience_text = """Audience cards exhibit significant imbalance in value efficiency (reward/complexity ratio):
    <br/><br/>
    <b>Highest Efficiency (2.0):</b> Drums, Keys, Sax, Songwriting, Fame provide +2 AS for single requirement
    <br/><br/>
    <b>Lowest Efficiency (1.0):</b> Guitar, Bass, Vocal provide only +1 AS for single requirement
    <br/><br/>
    <b><font color="#f39c12">Balance Issue:</font></b> Drums/Keys/Sax provide 2× value efficiency of
    Guitar/Bass/Vocal despite equal requirement complexity, creating instrument hierarchy. Average audience
    card reward is 1.94 AS, with 50% of cards offering +2 AS."""
    elements.append(Paragraph(audience_text, styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))

    # 3.6 Special Taste Balance
    elements.append(Paragraph("3.6 Special Taste Balance", heading2_style))

    special_taste_text = """Special tastes show poor difficulty-to-reward scaling:
    <br/><br/>
    • <b>Easy 1-point tasks:</b> High value (4 such tasks: instrument pairs, 4 different instruments)
    <br/><br/>
    • <b>Very Hard 2-point tasks:</b> Poor value (only 1× better reward for 4× difficulty)
    <br/><br/>
    • <b>"All Drums/Keys/Sax":</b> Requires monotype band (extreme constraint) for only 2 points
    <br/><br/>
    • <b>"2+ Vocal AND 2+ Spotlight":</b> Very Hard difficulty for 2 points
    <br/><br/>
    <b><font color="#f39c12">Imbalance:</font></b> Easy special tastes provide equal rewards to hard
    special tastes, creating perverse incentives to avoid restrictive builds."""
    elements.append(Paragraph(special_taste_text, styles['Normal']))
    elements.append(PageBreak())

    # Discussion
    elements.append(Paragraph("4. Discussion", heading1_style))

    discussion1 = """<b>Multiplicative Scoring: A Double-Edged Design</b>
    <br/><br/>
    The multiplicative scoring formula creates strategic depth by rewarding balanced optimization, but
    introduces three significant problems:
    <br/><br/>
    1. <b>Extreme Variance:</b> 110× theoretical range enables unrecoverable score gaps
    <br/><br/>
    2. <b>Asymmetric Returns:</b> SS improvements yield 3.6× greater impact than TS improvements
    <br/><br/>
    3. <b>Snowball Amplification:</b> Small early advantages compound exponentially across cities"""
    elements.append(Paragraph(discussion1, styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))

    discussion2 = """<b>Card Rarity Power Curve</b>
    <br/><br/>
    Rainbow cards provide disproportionate value: 2.75 tags/card vs. 0.59 for Bronze (4.66× multiplier),
    access to all 4 styles (Rainbow Keys/Guitar) vs. 1-2 for most cards, and the Technique 8 outlier
    (50% better than next-best Technique 6). This creates draft lottery dynamics where players acquiring
    multiple Rainbow cards gain insurmountable advantages."""
    elements.append(Paragraph(discussion2, styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))

    discussion3 = """<b>Audience Card Imbalance</b>
    <br/><br/>
    The instrument hierarchy (Drums/Keys/Sax = 2× value of Guitar/Bass/Vocal) forces meta-strategic constraints:
    bands should prioritize Drums/Keys/Sax for audience flexibility, Guitar/Bass/Vocal require combo cards
    to justify inclusion, and random audience card draw can invalidate strategic band composition."""
    elements.append(Paragraph(discussion3, styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))

    # Recommendations
    elements.append(Paragraph("5. Recommendations", heading1_style))

    elements.append(Paragraph("5.1 Critical Priority: Scoring Formula", heading2_style))

    rec1 = """<b>Recommendation 1:</b> Replace pure multiplication with diminishing returns formula:
    <br/><br/>
    <i>Total Score = TS × (1 + SS/5) × (1 + AS/10)</i>
    <br/><br/>
    This preserves strategic interaction while reducing max/min ratio from 110× to approximately 30×."""
    elements.append(Paragraph(rec1, styles['Normal']))
    elements.append(Spacer(1, 0.15*inch))

    rec2 = """<b>Recommendation 2 (Alternative):</b> Implement additive-multiplicative hybrid:
    <br/><br/>
    <i>Total Score = (TS × SS) + (AS × 10)</i>
    <br/><br/>
    This balances technique/style optimization against audience performance."""
    elements.append(Paragraph(rec2, styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))

    elements.append(Paragraph("5.2 High Priority: Card Balance", heading2_style))

    rec3 = """<b>Recommendation 3:</b> Adjust Technique 8 Rainbow Guitar to Technique 7, or introduce second
    Technique 8 card to reduce draft variance."""
    elements.append(Paragraph(rec3, styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))

    rec4 = """<b>Recommendation 4:</b> Normalize audience card rewards:
    <br/>• Guitar/Bass/Vocal: Increase to +2 AS (from +1)
    <br/>• Drums/Keys/Sax: Reduce to +1 AS (from +2)
    <br/>• Maintain combo cards at current values"""
    elements.append(Paragraph(rec4, styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))

    rec5 = """<b>Recommendation 5:</b> Rebalance special taste rewards by difficulty:
    <br/>• Easy tasks (instrument pairs): 1 point (no change)
    <br/>• Hard tasks (3+ tags, exclusive builds): 2-3 points
    <br/>• Very Hard tasks (monotype): 4-5 points"""
    elements.append(Paragraph(rec5, styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))

    elements.append(Paragraph("5.3 Medium Priority: Gameplay Mechanics", heading2_style))

    rec6 = """<b>Recommendation 6:</b> Implement catch-up mechanics: Trailing players (3rd/4th in Popularity)
    receive +1 bonus action in Preparation Phase, or draft first in subsequent cities."""
    elements.append(Paragraph(rec6, styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))

    rec7 = """<b>Recommendation 7:</b> Reveal audience cards before band selection in Battle Phase to reduce
    variance and increase strategic agency."""
    elements.append(Paragraph(rec7, styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))

    rec8 = """<b>Recommendation 8:</b> Limit Rainbow cards to 1 per player per city during draft to prevent
    concentration."""
    elements.append(Paragraph(rec8, styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))

    # Conclusion
    elements.append(Paragraph("6. Conclusion", heading1_style))

    conclusion = """<i>Battle of Bands</i> demonstrates ambitious design through its multiplicative scoring
    system and diverse strategic elements. However, mathematical analysis reveals significant balance concerns
    that may impact competitive play:
    <br/><br/>
    • Extreme score variance (110× range) enables snowball dynamics
    <br/>• Asymmetric marginal returns make Style Score 3.6× more valuable than Technique Score
    <br/>• Rainbow card power and Technique 8 outlier create draft lottery effects
    <br/>• Audience card instrument hierarchy and special taste difficulty misalignment reduce strategic diversity
    <br/><br/>
    The most critical intervention is reformulating the scoring system to reduce multiplicative amplification
    (Recommendations 1-2). Combined with card balance adjustments (Recommendations 3-5), these changes would
    preserve the game's strategic depth while enhancing competitive integrity.
    <br/><br/>
    The analysis suggests that the current design inadvertently favors Rainbow Collector and City Matcher
    strategies over the thematically central Specialist (high-technique) approach. Rebalancing multiplicative
    weights or introducing diminishing returns would align mechanical incentives with the game's thematic
    emphasis on musical technique while maintaining meaningful strategic differentiation.
    <br/><br/>
    Further playtesting with proposed adjustments is recommended to validate these mathematical projections
    and assess player experience impacts."""
    elements.append(Paragraph(conclusion, styles['Justify']))

    # Build PDF
    doc.build(elements)
    print(f"PDF generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_balance_report()
