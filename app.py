from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.markdown("<a id='top'></a>", unsafe_allow_html=True) # top anchor



# Custom Links Color
st.markdown("""
<style>
/* Change color of all links */
a {
    color: #7dff9f !important;   /* light green */
    text-decoration: none;
}

/* Change color of links when hovered */
a:hover {
    color: #25cf52 !important;   /* darker green on hover */
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)


# Custom Expander Colour
st.markdown("""
<style>
/* Expander header */
details > summary {
    background-color: #00bf86 !important;
    color: black !important;
    border-radius: 6px;
    padding: 8px;
    font-weight: 600;
}

/* Expander body */
details > div {
    background-color: #0b2033 !important;
    border-radius: 6px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown(
    """
    <div class="navbar">
        <input type="checkbox" id="menu-toggle">
    
        <label for="menu-toggle" class="hamburger">
            <span></span>
            <span></span>
            <span></span>
        </label>
    
        <div class="nav-left">
            <a href="#projects">Projects</a>
            <a href="#work-experience">Job Experience</a>
            <a href="#skills">Skills</a>
            <a href="#education">Education and Languages</a>
            <a href="#hobbys">Hobbys</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)


# Footer
st.markdown(
    """
    <style>
        .fixed-footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: #0b2033;
            color: #eeeeee;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }
    </style>

    <div class="fixed-footer">
        Created by Jule Blokinsky © 2026
    </div>
    """,
    unsafe_allow_html=True
)



# more emojii shortcodes https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":octopus:", layout="wide")

# animation load function
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)





local_css("styles/style.css")

# ---- LOAD ASSETS ----

# animations
lottie_coding = load_lottieurl("https://lottie.host/fba54955-dcfa-43c9-b322-c1e3f8c22951/c38a9aTuVF.json")
lottie_job = load_lottieurl("https://lottie.host/80c4e616-27b7-49ed-be7d-5ab446229f08/A76ej0sda9.json")


# images
img_contact_form = Image.open("assets/Me2.jpg")
img_hobby = Image.open("assets/jule3.jpg")

# ---- HEADER SECTION ----

with st.container():
    left_column, spacer, right_column = st.columns((2, 0.1, 1))
    with left_column:
        st.subheader("Hi, I am Jule Blokinsky 🧑‍💻 ")
        st.title("Sales professional in transition to IT")
        st.write("Inspired by technology, committed to ethical NLP sales.")
        st.write("35 years old, 20 years of hands-on job experience")
        st.write("##")
        # st.write("[My LinkedIn >](https://www.linkedin.com/in/jul3sky/)")

        # LinkedIn Button
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/jul3sky/" target="_blank">
                <div style="
                    display:inline-block;
                    background-color:#0A66C2;
                    color:white;
                    padding:10px 20px;
                    border-radius:6px;
                    font-weight:600;
                    text-align:center;
                    text-decoration:none;
                    cursor:pointer;">
                    My LinkedIn >
                </div>
            </a>
            """,
            unsafe_allow_html=True
        )

            

    with right_column:
        st.lottie(lottie_coding, height=300, key="techsales") # animation

# ---- WHAT I DO ----

with st.container():
    st.write("----") # creates a tiny horizontal line
    left_column, right_column = st.columns(2, gap="medium")
    with left_column:
        st.header("Who I Am")
        st.write('##') # to add some space to the next element
        st.write("""
                • I am a driven and committed person with a genuine interest in technology and people. """)
        st.write("""
                • I have built up solid experience of working closely with customers, understanding their needs and offering solutions that create added value. """)
        st.write("""
                • I see myself as a quick and flexible learner. """)
        st.write("""         
                • I thrive in roles where I am challenged. """)
        st.write("""
                • My experience as a salesperson has taught me the importance of building trusting relationships, both with customers and colleagues. """)

    with right_column:
        st.write("##")
        st.write("##")
        st.write("""
                • I am responsive and have the ability to communicate in a way that makes people feel seen and understood. """)
        st.write("""
                • I create a positive customer experience and increasing sales.""")
        st.write("""        
                • I am also used to working in dynamic environments where multitasking and problem solving are a natural part of everyday life.""")
        st.write(""" • I am stress-resistant and flexible.""")
        st.write(""" • I see technology as my hobby, not just a part of my job.""")

# ---- MY TECHNICAL EXPERIENCE ----
st.write("----")
st.markdown('<div id="projects"></div>', unsafe_allow_html=True) # connect the section with navbar menu

with st.container():
    st.header("My Projects")
    st.write("##")
    image_column, spacer, text_column = st.columns((1, 0.1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Technical Experience")
        st.header("Technical Support Project – JobSkillShare Labs ") # TechSupport Experience
        st.markdown("##### Apr 2025 – Sep 2025")

        st.write("During this project, I immersed myself in the day‑to‑day world of IT support and learned what it really means to keep systems — and people — running smoothly. It wasn’t just a checklist of tasks; it felt like stepping into the rhythm of a real support environment and growing with every challenge.") 
        with st.expander("Continue reading"): 
            st.write(""" I started by getting hands‑on with Windows OS troubleshooting, learning how to diagnose issues from slow performance to system errors and understanding the “why” behind each fix. From there, I moved deeper into the infrastructure side, working with Active Directory to manage users, groups, and permissions — the backbone of any well‑organized environment.

As the project progressed, I began handling simulated tickets through Jira, which taught me how to prioritize, communicate clearly, and document solutions the way real support teams do. Networking became another major part of the journey: I learned to break down problems involving DNS, DHCP, TCP/IP, and trace issues from the workstation all the way to the network layer.

I also spent time installing and configuring software, managing firewall settings, and using remote support tools to assist “end users” from a distance — a skill that feels almost second nature now. Hardware diagnostics rounded out the experience, giving me a full view of how physical components tie into the bigger picture.

Throughout the project, I made it a habit to create clear, structured documentation, not just for myself but as if I were handing it off to a real team. That practice helped me think like a technician who supports others, not just systems.

Overall, this project was a genuine journey — one that strengthened my technical foundation, sharpened my problem‑solving mindset, and confirmed how much I enjoy working in IT support. """)

        st.write("##")
        st.header("Cybersecurity 101 – TryHackMe.com Labs ") # Cybersecurity Experience
        st.markdown("##### Apr 2025 – Sep 2025")

        st.write("This project marked the moment I stepped beyond curiosity and into the real, hands‑on world of cybersecurity. Working through TryHackMe’s virtual labs felt less like a course and more like entering a new landscape — one where every challenge taught me how systems work, how they break, and how to protect them.")
        with st.expander("Continue reading"):
            st.write("""I began by building a strong foundation in Linux fundamentals, getting comfortable with the command line, navigating the file system, and understanding how the operating system behaves under the hood. That experience made the environment feel less like a black box and more like a place I could confidently explore.

From there, I moved into Windows and Active Directory hardening, learning how attackers target these systems and how defenders lock them down. It was the first time I truly saw how security decisions ripple across an entire environment.

Networking quickly became another major pillar of the journey. I studied core and secure protocols, then applied that knowledge through traffic analysis using tools like Wireshark, Tcpdump, and Nmap. Seeing packets move across a network — and understanding what they reveal — was a turning point in how I viewed system communication.

I also dove into cryptography, learning how encryption, encoding, and hashing protect data and where weaknesses can appear. That naturally led into exploitation and web‑hacking basics, where I explored real‑world vulnerabilities and began to understand the mindset behind web application attacks.

The labs then split into two complementary paths:

•  Offensive security, where I practiced using tools common in penetration testing

•  Defensive security, where I learned about SOC operations, digital forensics, and incident response

This dual perspective helped me appreciate both sides of the cybersecurity equation — how attackers think and how defenders respond.

I wrapped up the project by working with security solutions such as firewalls, IDS, vulnerability scanners, and SIEM platforms. These tools tied everything together, showing how organizations detect, analyze, and respond to threats in real time.

What started as a structured module ended up sparking a genuine passion. Since completing it, I’ve continued exploring cybersecurity through books (including the Linux Professionals series), deeper Linux studies, shell scripting, advanced networking concepts, and the broader logic behind protocols and topologies. I’m also actively developing a “hacker mindset” — not to break things, but to understand how attackers think so I can better defend systems and networks.

This experience didn’t just teach me skills; it reshaped how I see technology, security, and the constant battle between the two.""")



# ---- WORK EXPERIENCE ----

st.write("----")
st.markdown('<div id="work-experience"></div>', unsafe_allow_html=True) # connect the section with navbar menu


with st.container():
    st.header("Job Experience")
    st.write("##")
    left_column, spacer, right_column = st.columns((2, 0.1, 1))
    with left_column:
        st.subheader("Sales Assistant - Fiskars Group") # Sales Fiskars
        st.markdown("#### Part-Time:  jan 2025 - apr 2025")
        st.write("##### Stockholm Sweden")
        st.write("Temporary Sales Assistant practice at one of the Fiskars Group shops with focus on the Swedish-speaking performance.")
        st.write("##")
        st.subheader("Personal Care Assistant - Assistans I Balans") # Personal Assistant PA
        st.markdown("#### Part-Time: may 2024 - apr 2025")
        st.write("##### Stockholm Sweden")
        st.write("Provided assistance with daily routines, such as personal care, exercise, cooking, etc.")
        with st.expander("Read full job description"):  # PA job description
            st.write("""• Ensured that all lifting, moving, and exercise equipment was in optimal condition and ready to use.""")
            st.write("""• Accompanied my client socially.""")
            st.write("""• Created a positive atmosphere in the work environment.""")
            st.write("""• Demonstrated good results in performing 2-3 tasks simultaneously and developed a warm and friendly relationship with my client.""")
        with st.expander("What I learned from this role"): # PA job insights
            st.write("""Working as a Personal Care Assistant taught me far more than practical routines — it showed me how meaningful everyday life can become when approached with patience, empathy, and genuine connection. I learned that supporting a person with functional disabilities isn’t just about tasks; it can grow into a positive, social interaction that brings joy to both sides. This role pushed me to become a better listener, to respond quickly and thoughtfully, and to stay attentive to even the smallest details so my client’s day felt complete and fulfilling. Most importantly, it deepened my awareness of how much the lives and experiences of people with disabilities matter, and how essential it is to support their independence, dignity, and quality of life.""")

        st.write("##")
        st.subheader("Commercial Buyer - Veo Worldwide Services") # Commercial Buyer CB 
        st.write("https://veoworldwide.com/") 
        st.markdown("#### Full-Time: may 2021 - may 2022")
        st.write("##### Lviv Ukraine")
        st.write("Negotiated pricing and purchasing terms, ensuring profitable margins while maintaining strong supplier relationships.")
        with st.expander("Read full job description"): # CB job description
            st.write("""• Managed the acquisition of surplus stock from suppliers for resale through discount retail channels.""") 
            st.write("""• Took part in coordination of delivery logistics to move goods efficiently to end purchasers, resolving challenges related to timelines, prepayment conditions, and transportation.""")
            st.write("""• Oversaw quality checks to ensure all products met the standards required by the retail chain, maintaining consistency and reliability throughout the buying process.""")
        with st.expander("What I learned from this role"): # CB job insights
            st.write("""Working as a Commercial Buyer taught me how much impact careful preparation and structured teamwork have on the entire purchasing process. I joined the project in Ukraine from the very beginning, which meant I experienced every stage firsthand: from sourcing and building a database of FMCG producers and wholesalers, to prospecting leads, and finally moving into active buying. Through this, I learned how essential it is to gather precise, relevant information about each potential supplier before making any decisions. Good data doesn’t just improve accuracy; it saves time and leads to stronger, more targeted purchasing outcomes. I also discovered the value of competitive collaboration, where top performers openly support the rest of the team so everyone can reach higher results together. This role strengthened my analytical mindset, my attention to detail, and my appreciation for a team culture built on shared success.""")

        st.write("##")
        st.subheader("VSAT Service Delivery Coordinator - Altegrosky") # VSAT service coordinator
        st.write("https://altegrosky.ru/eng-eng/")
        st.markdown("#### Full-Time: sep 2017 - feb 2020")
        st.write("##### Moscow Russia")
        st.write("Coordinated end‑to‑end delivery of VSAT equipment to remote sites across the Russian North, ensuring timely arrival despite challenging weather and logistical constraints.")
        with st.expander("Read full job description"):  # VSAT service coordinator job description
            st.write("""• Managed routing adjustments.""")
            st.write("""• Synchronized equipment delivery with technician deployment.""")
            st.write("""• Oversaw all travel and accommodation arrangements.""") 
            st.write("""• Maintained full documentation flow, including service level agreements, equipment inventories, and invoice processing, ensuring accuracy and compliance throughout the service delivery cycle.""")
        with st.expander("What I learned from this role"): # job insights
            st.write("""This role taught me the true importance of planning, precision, and coordination in service delivery. Every order began with verifying that each component of the network equipment was present and accounted for — because when a VSAT kit was being shipped to a remote site accessible only by helicopter, even a missing screw or cable could delay the entire deployment and lead to extremely costly re‑deliveries. I learned to take full ownership of this process, double‑checking every detail even when the warehouse team had already done their part. I also gained a strong understanding of how critical it is to synchronize equipment delivery with technician availability. VSAT technicians were limited and often responsible for multiple sites in the same region, so staying aware of their locations, schedules, and potential extra tasks became essential. On top of that, the unpredictable northern weather added another layer of complexity — a technician could easily get stuck in one area if helicopter flights were grounded. Navigating all these factors taught me how to manage uncertainty, plan ahead, and keep operations running smoothly despite challenging conditions.""")

        st.write("##")
        st.subheader("Brand Promoter - MTS(Mobile TeleSystems)") # Promoter
        st.markdown("#### Contract: nov 2016 - jun 2017")
        st.write("##### Moscow Russia")
        st.write("Acted as the face of the mobile operator during field activations in high‑visibility public spaces.")
        with st.expander("Read full job description"): # # Promoter job description
            st.write("""• Engaged diverse audiences, increased brand awareness, and drove subscriber growth through personalized communication.""")
            st.write("""• Oversaw inventory of promotional materials, ensuring accurate tracking and responsible handling.""")
        with st.expander("What I learned from this role"):
            st.write("""Developed the ability to confidently present and explain technological products in public settings, clearly communicating the benefits of mobile subscriptions to diverse audiences.""")

        st.write("##")
        st.subheader("Sales Assistant > Senior Sales Assistant - ZARA Inditex.inc") # Sales assistant
        st.markdown("#### Full-Time: mar 2013 - may 2016")
        st.write("##### Lviv Ukraine")
        st.write("Applied a consultative sales approach to understand customer needs and recommend the most suitable offers.")
        with st.expander("Read full job description"): # Sales assistant job description
            st.write("""• Welcomed customers and supported them with product questions, selection, and purchasing decisions.""")
            st.write("""• Provided clear and accurate information regarding product features, availability, and pricing.""")
            st.write("""• Used store systems to verify stock levels and ensure correct visual merchandising and product presentation.""")
            st.write("""• Trained new employees with focus on learning of sales techniques.""")
        with st.expander("What I learned from this role"):
            st.write("""Gained a deep understanding of sales principles, including how to identify customer needs and guide them toward the right products.

Learned to engage with customers in a natural, friendly, and confident manner, building trust and creating a positive shopping experience.

Developed strong questioning techniques to uncover customer preferences and tailor recommendations effectively.

Trained new employees in sales methods and customer interaction, strengthening my communication and leadership skills.

Discovered a genuine interest in men’s fashion, which enhanced my product knowledge and enthusiasm on the sales floor.""")


        st.write("##")
        st.subheader("Visual Merchandiser / Junior Trade Agent") # Trade Agent VM
        st.write("#### Beverage Company OVERCO")
        st.markdown("#### Part-Time: mar 2008 - mar 2012")
        st.write("##### Lviv Ukraine")
        st.write("Physical B2B (HORECA) sales, implementation and maintenance of promotional and advertising materials on the Sales spot.")
        
        with st.expander("What I learned from this role"):
            st.write("""I gained a strong understanding of how product placement influences customer perception and purchasing behavior, especially within HORECA environments.

Learned the importance of well‑positioned POS materials in strengthening brand visibility and driving sales.

Developed practical skills in implementing, maintaining, and optimizing promotional displays to meet brand standards.

Expanded my knowledge of B2B sales by supporting a Trade Agent, ensuring consistent product availability and a full assortment across sales points.

Built experience in stock control, monitoring inventory levels, and coordinating timely replenishment, including the introduction of new products.

Strengthened collaboration and communication skills through close cooperation with retail partners and on‑site staff.""")



        st.write("##")
        st.subheader("Shop Assistant")
        st.write("#### A Shop in Ukraine")
        st.markdown("#### Part-Time: may 2006 - aug 2007")
        st.write("##### Lviv Ukraine")
        st.write("Built a strong foundation in retail routines, responsibility, and reliability—skills that supported my growth in later customer‑facing roles.")
        
        with st.expander("What I learned from this role"):
            st.write("""Gained hands‑on experience with cashier operations, including handling payments accurately and efficiently.

Learned to deliver polite, attentive customer service and assist shoppers with their needs in a friendly and professional manner.

Developed technical skills by operating a Xerox machine and managing basic printing, copying, and document‑handling tasks.""")


    with right_column:
        st.lottie(lottie_job, height=300, key="job") # animation

# ---- SKILLS ----
st.write("----")
st.markdown('<div id="skills"></div>', unsafe_allow_html=True) # comnnect the section with navbar menu

with st.container():
    st.header("My Skills")  
    st.write("##")
    left_column, spacer, right_column = st.columns((1, 0.1, 1))
    with left_column:
        st.markdown("#### Tech Skills")
        st.write("• Windows security & Active Directory")
        st.write("• Linux Essentials, CLI")
        st.write("• Python, HTML/CSS")
        st.write("• Networking (DNS, DHCP, TCP/IP)")
        st.write("• Traffic analysis basics (Wireshark, Tcpdump, Nmap)")
        st.write("• Web vulnerabilities & exploitation basics ")
        st.write("• Offensive security tools ")
        st.write("• Firewalls, IDS, vulnerability scanners, SIEM")
        st.write("• Cryptography basics ")

    with right_column:
        st.markdown("#### Soft Skills")
        st.write("• Active listening")
        st.write("• Empathy and client‑focused communication")
        st.write("• Attention to detail")
        st.write("• Time management")
        st.write("• Planning and prioritization")
        st.write("• Problem‑solving")
        st.write("• Analytical thinking")
        st.write("• Reliability under pressure")
        st.write("• Team collaboration")



# ---- EDUCATION AND LANGUAGES -----
st.write("----")
st.markdown('<div id="education"></div>', unsafe_allow_html=True) # comnnect the section with navbar menu

with st.container():
    st.header("Education and Languages")
    st.write("##")
    left_column, spacer, center_column, spacer, right_column = st.columns((1, 0.1, 1, 0.1, 1))
    with left_column:
        st.markdown("### High School:")
        st.write("#### Gymnasium #45")
        st.write("With advanced studies of English")
        st.write("1997-2007")
        st.write("Lviv, Ukraine")

    with center_column:
        st.markdown("### Languages:")
        st.write("##### English")
        st.write("Full working proficiency")
        
        st.write("##### Swedish")
        st.write("Full working proficiency")
    
        st.write("##### Ukrainian")
        st.write("Native / bilingual")
        
        st.write("##### Russian")
        st.write("Native / bilingual")


    with right_column:
        st.markdown("### Courses")

        courses = [
            ("Teaching of English as Foreign Language", "A-Level School, 2008"),
            ("Neurolinguistic Programming (Practitioner)", "Moscow Psychoanalysis Institute, 2011"),
            ("Web Design", "Mail.ru Academy, 2017"),
            ("UX/UI", "Mail.ru Academy, 2017"),
            ("Mobile Application Design", "Mail.ru Academy, 2017"),
            ("Marketing and Communications", "IBMI, 2020"),
            ("International Trading", "SME Trade Academy, 2021"),
            ("Cybersecurity 101", "TryHackMe, 2025"),
        ]

        for title, school in reversed(courses):
            st.write(f"#### {title}")
            st.write(school)




#----HOBBYS-----
st.write("----")
st.markdown('<h2 id="hobbys">Hobbys</h2>', unsafe_allow_html=True) # comnnect the section with navbar menu

with st.container():
    st.write("##")
    text_column, spacer, image_column = st.columns((((1, 0.1, 1))))

    with text_column:
        st.markdown("#### I am a self-taught artist")
        st.write("I’m a self‑taught artist with a lifelong passion for drawing, painting, embroidery, and creating objects from colorful paper. I also enjoy digital design and often experiment with different styles and techniques. Art has been a part of my life since childhood, even though it was mostly recognized only within my family, who encouraged me to pursue a more “practical” educational path. Despite that, creativity has always stayed with me — through good times and difficult ones — becoming a therapeutic space where I continue to grow and explore. I also run a small Instagram project where I express my fascination with the versatility of circular form.")
        # st.write("[My Artsy Instagram >](https://instagram.com/__solis.spiro?igsh=MTAzZ3kwdnQwbDI2ag==)")

        # Instagram Button
        st.markdown(
            """
            <a href="https://instagram.com/__solis.spiro?igsh=MTAzZ3kwdnQwbDI2ag==" target="_blank">
                <div style="
                    display:inline-block;
                    background-color:#0092b4;
                    color:white;
                    padding:10px 20px;
                    border-radius:6px;
                    font-weight:600;
                    text-align:center;
                    text-decoration:none;
                    cursor:pointer;">
                    My Artsy Instagram >
                </div>
            </a>
            """,
            unsafe_allow_html=True
        )

    with image_column:
        st.image(img_hobby)





# ---- CONTACT ----
st.write("----")
st.markdown('<div id="contact"></div>', unsafe_allow_html=True) # connect the section with navbar menu

with st.container():
    st.header("Get In Touch With Me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/3565291d5302d775cea9f27bb310452e" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Full Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()






#ScrollTop Button
st.markdown(
    """
    <style>
        #scrollTopBtn {
            position: fixed;
            bottom: 40px;
            right: 40px;
            z-index: 99;
            background-color: #00bf86;
            color: white;
            border: none;
            padding: 12px 21px;
            border-radius: 50%;
            font-size: 18px;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        #scrollTopBtn:hover {
            background-color: #084a8f;
        }
    </style>

    <a href="#top">
        <button id="scrollTopBtn">↑</button>
    </a>
    """,
    unsafe_allow_html=True
)












