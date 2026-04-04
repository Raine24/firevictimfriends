import shutil
import os

src_img_paths = [
    "C:/Users/Baker/.gemini/antigravity/brain/b4cdb2c6-ce81-4084-8658-af6780d31ac2/prevention_hero_1775143977747.png",
    "C:/Users/Baker/.gemini/antigravity/brain/b4cdb2c6-ce81-4084-8658-af6780d31ac2/prevention_row1_1775143998423.png",
    "C:/Users/Baker/.gemini/antigravity/brain/b4cdb2c6-ce81-4084-8658-af6780d31ac2/prevention_row2_1775144016879.png",
    "C:/Users/Baker/.gemini/antigravity/brain/b4cdb2c6-ce81-4084-8658-af6780d31ac2/prevention_row3_1775144037225.png"
]

os.makedirs('images', exist_ok=True)
paths_to_replace = []

for idx, p in enumerate(src_img_paths):
    dest = f"images/prev_{idx}.png"
    if os.path.exists(p):
        shutil.copy(p, dest)
    paths_to_replace.append(dest)

with open('emergency-relief.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <title>
html = html.replace('<title>Emergency Relief Program | Fire Victim Friends</title>', '<title>Fire Prevention & Awareness | Fire Victim Friends</title>')

# Replace badge
html = html.replace('<i class="ph-bold ph-first-aid-kit"></i> 01. Emergency Support', '<i class="ph-bold ph-shield-star"></i> 02. Proactive Prevention')

# Replace Hero Title
html = html.replace('Into the <span style="background: linear-gradient(135deg, var(--color-primary-orange), var(--color-primary-red)); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;">Aftermath.</span>', 
                    'Stopping the <span style="background: linear-gradient(135deg, var(--color-primary-orange), var(--color-primary-red)); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;">Spark.</span>')

# Replace Hero Description
html = html.replace('When flames decimate homes, schools, and markets, the immediate aftermath is defined by chaos. We deploy directly to ground zero, providing vital emotional and physical security to stabilize lives when they need it most.',
                    'Disaster is best stopped before it begins. We actively educate high-risk communities and integrate cutting-edge fire safety protocols directly into the most vulnerable infrastructures to save lives.')

# Replace Hero Image Background
html = html.replace("url('https://i.imgur.com/C4ffpDA.jpg')", f"url('{paths_to_replace[0]}')")

# Floating pills
html = html.replace('<i class="ph-fill ph-ambulance"></i> Rapid Deployment', '<i class="ph-fill ph-shield-check"></i> Risk Assessments')
html = html.replace('<i class="ph-fill ph-house-line"></i> Immediate Shelter', '<i class="ph-fill ph-users-three"></i> Community Training')
html = html.replace('<i class="ph-fill ph-check-circle"></i> Sustainment Prep', '<i class="ph-fill ph-fire-extinguisher"></i> Safety Protocols')

# Fast Facts
html = html.replace('Under 24 Hours', 'High-Risk Zones')
html = html.replace('Average crisis deployment timeframe.', 'Focused on the most vulnerable slums and markets.')

html = html.replace('Vital Triage', 'Safety Workshops')
html = html.replace('Immediate medical and mental lifelines.', 'Weekly immersive safety demonstrations.')

html = html.replace('Sustainment Kits', 'Early Detection')
html = html.replace('Food, blankets, and stabilization supplies.', 'Installing alarms and basic suppression tools.')

# Phase 01
html = html.replace('PHASE 01: THE FRONT LOAD', 'PHASE 01: IDENTIFICATION')
html = html.replace('<h3>Sustainment &amp; Critical Supplies</h3>', '<h3>Mapping Vulnerability</h3>')
html = html.replace('<h3>Sustainment & Critical Supplies</h3>', '<h3>Mapping Vulnerability</h3>')
html = html.replace('<p>Within hours of a catastrophic fire, affected families lose access to fundamental human necessities—water, food, and protective clothing. The disorientation of losing an entire livelihood requires immediate intervention.</p>', '<p>Before we can prevent a fire, we must identify where it is most likely to strike. Many communities lack basic zoning, meaning a single spark can devastate hundreds of interconnected structures.</p>')
html = html.replace('<p>Our frontline teams bypass logistical delays by maintaining pre-stocked active response depots across Uganda. We actively distribute deeply comprehensive "Sustainment Kits" tailored specifically to stabilize individuals transitioning through the acute shock phase of disaster.</p>', '<p>Our field teams conduct rigorous safety audits in dense markets, informal settlements, and schools. We identify critical hazards such as overloaded electrical nodes, illegal connections, and highly combustible building materials.</p>')
html = html.replace('<li>High-caloric, non-perishable daily meal rations for families of up to 6.</li>', '<li>Comprehensive drone and ground mapping of high-density zones.</li>')
html = html.replace('<li>Thermal and weather-resistant heavy blankets.</li>', '<li>Electrical safety inspections and load assessments.</li>')
html = html.replace('<li>Clean clothing bundles sorted by gender and age groups.</li>', '<li>Identifying and mapping clear evacuation routes.</li>')
html = html.replace('https://i.imgur.com/cbEAkJA.jpg', paths_to_replace[1])

# Phase 02
html = html.replace('PHASE 02: STABILIZATION', 'PHASE 02: EDUCATION')
html = html.replace('<h3>Medical Triage &amp; Mental Lifelines</h3>', '<h3>Community Workshops</h3>')
html = html.replace('<h3>Medical Triage & Mental Lifelines</h3>', '<h3>Community Workshops</h3>')
html = html.replace('<p>To view disaster through a purely physical lens is a massive mistake. While thermal burns and smoke inhalation require immediate, aggressive medical triage, the destruction of a home shatters psychological stability entirely.</p>', '<p>Knowledge is the most powerful fire extinguisher. Many devastating blazes begin simply because individuals do not understand basic combustion triggers or how to safely smother small flames before they spread.</p>')
html = html.replace('<p>Our integrated emergency deployment units feature both trauma medics and psychiatric first-aid responders. We treat the unseen injuries simultaneously with the physical, preventing the onset of long-term PTSD right at ground zero.</p>', '<p>We host dynamic, hands-on safety workshops prioritizing youth, mothers, and shop owners. Our instructors demonstrate safe cooking practices, electrical load management, and the proper use of emergency suppression tools.</p>')
html = html.replace('<li>Instant coordination with regional ambulance networks.</li>', '<li>Hands-on fire extinguisher and sand-bucket training.</li>')
html = html.replace('<li>On-site burn treatments and respiratory therapy administration.</li>', '<li>Evacuation drills tailored for schools and marketplaces.</li>')
html = html.replace('<li>Immediate trauma counseling tailored specifically for children.</li>', '<li>Safety certifications for local community leaders.</li>')
html = html.replace('https://i.imgur.com/TGIzqh8.jpg', paths_to_replace[2])

# Phase 03
html = html.replace('PHASE 03: SECURE FOUNDATIONS', 'PHASE 03: INFRASTRUCTURE')
html = html.replace('<h3>Rapid Deployment Housing</h3>', '<h3>Immediate Safeguards</h3>')
html = html.replace('<p>A burnt structure leaves individuals completely vulnerable to the elements, secondary infections, and rampant further risks. Sleep deprivation combined with physical exposure multiplies the casualty rate of any disaster exponentially.</p>', '<p>Education without the proper tools is incomplete. We believe every home and business deserves the basic right to reliable and immediate fire suppression infrastructure.</p>')
html = html.replace('<p>We provide rapid-deployment emergency temporary shelters that guarantee a safe, fully insulated micro-environment. This guarantees warmth and dignity, allowing families to physically sleep, regroup, and begin assessing their path to long-term recovery.</p>', '<p>We permanently boost the safety foundation of a community by democratizing access to quality fire-fighting equipment. We install state-of-the-art smoke detectors and distribute industrial-grade extinguishers to key hubs.</p>')
html = html.replace('<li>Weather-proof, dual-layer active response family tents.</li>', '<li>Distribution of ABC dry chemical powder extinguishers.</li>')
html = html.replace('<li>Coordination with local municipality for secure zoning.</li>', '<li>Installation of sensitive, battery-operated smoke alarms.</li>')
html = html.replace('<li>Hygienic sanitation kits to prevent secondary localized outbreaks.</li>', '<li>Strategic placement of communal fire sand/water stations.</li>')
html = html.replace('https://i.imgur.com/upniMrK.jpg', paths_to_replace[3])

# Metrics
html = html.replace('4,000+', '50,000+')
html = html.replace('Individuals Relocated', 'Citizens Educated')
html = html.replace('12,500', '500+')
html = html.replace('Meals Distributed', 'Active Workshops')
html = html.replace('75+', '10,000+')
html = html.replace('Schools Restored', 'Extinguishers Deployed')

# CTA
html = html.replace('The Front Line<br>is Calling.', 'Prevention is<br>the Cure.')
html = html.replace('Stop observing and start deploying. Equip our crisis teams with the heavy funding required to turn total chaos back into control.', 'A single spark does not have to become a tragedy. Equip vulnerable communities with the knowledge and tools to save themselves.')
html = html.replace('FUND THE FRONTLINE NOW', 'FUND PREVENTION NOW')

# Fix self referencing active links in nav if any (not strictly needed but good)
html = html.replace('Emergency Relief Program | Fire Victim Friends', 'Fire Prevention & Awareness | Fire Victim Friends')

with open('fire-prevention.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS")
