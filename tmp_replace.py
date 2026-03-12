import re
import os

filepath = "c:\\Users\\silas\\Documents\\GitHub\\miply-website\\what-is-mip.html"
with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

new_html = """    <!-- HERO SECTION -->
    <header class="pt-32 pb-20 px-4 bg-dot-grid">
        <div class="max-w-7xl mx-auto">
            <h1 class="text-4xl md:text-6xl font-black text-theme-dark leading-[1.1] mb-6">
                Managed Intelligence Provider
            </h1>
            <p class="text-xl md:text-2xl font-bold text-theme-dark mb-8 leading-relaxed max-w-4xl">
                A Managed Intelligence Provider designs, structures, and operates intelligence-driven systems that measurably improve business performance.
            </p>
            <div class="prose prose-lg text-slate-600 max-w-4xl mb-8 space-y-6">
                <p>
                    The MSP model was built around infrastructure stability and system reliability. That foundation remains essential. The next phase of the industry requires more than uptime. It requires structured data environments, workflow orchestration, and applied intelligence that improves how businesses operate.
                </p>
                <p class="font-bold text-xl text-theme-dark">
                    A Managed Intelligence Provider engineers that next layer.
                </p>
            </div>
        </div>
    </header>

    <!-- SECTION 1: ARCHITECTURE MODEL -->
    <section class="py-20 border-t border-slate-200 bg-theme-card">
        <div class="max-w-7xl mx-auto px-4">
            <div class="text-center mb-16">
                <span class="inline-block font-hand text-theme-blue text-xl font-bold mb-4 transform -rotate-1">
                    <i class="fas fa-layer-group"></i> Architecture Model
                </span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-theme-dark mb-6">The Four-Layer Architecture Model</h2>
                <p class="text-lg text-slate-600 max-w-3xl mx-auto">
                    A Managed Intelligence Provider operates across four integrated layers. Intelligence becomes durable only when architecture is disciplined.
                </p>
            </div>

            <!-- Graphic representation: Stacked levels -->
            <div class="max-w-4xl mx-auto flex flex-col gap-6 relative mb-16 px-4 md:px-0">
                <!-- Data flow line behind -->
                <div class="absolute left-[calc(2rem+1rem)] md:left-24 top-10 bottom-10 w-1 bg-gradient-to-b from-theme-blue to-slate-200 z-0"></div>
                
                <!-- Layer 4: Intelligence -->
                <div class="sketch-card border-sketch-5 p-8 relative z-10 bg-theme-card ml-8 md:ml-16 transform transition-transform hover:-translate-y-1">
                    <div class="absolute -left-12 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-theme-blue border-4 border-theme-card flex items-center justify-center text-white font-bold text-sm shadow-sm">4</div>
                    <div class="flex flex-col md:flex-row items-start gap-4">
                        <div class="text-3xl text-theme-blue mt-1"><i class="fas fa-brain"></i></div>
                        <div>
                            <h3 class="text-2xl font-bold text-theme-dark mb-2">Intelligence Layer</h3>
                            <p class="text-theme-dark font-medium mb-2">Decision-support systems, AI agents, predictive analytics, performance dashboards.</p>
                            <p class="text-slate-600">Intelligence is embedded where it measurably improves speed, cost, or accuracy.</p>
                        </div>
                    </div>
                </div>

                <!-- Layer 3: Workflow Orchestration -->
                <div class="sketch-card border-sketch-4 p-8 relative z-10 bg-theme-card ml-8 md:ml-16 transform transition-transform hover:-translate-y-1">
                    <div class="absolute -left-12 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-slate-700 border-4 border-theme-card flex items-center justify-center text-white font-bold text-sm shadow-sm">3</div>
                    <div class="flex flex-col md:flex-row items-start gap-4">
                        <div class="text-3xl text-slate-700 mt-1"><i class="fas fa-project-diagram"></i></div>
                        <div>
                            <h3 class="text-2xl font-bold text-theme-dark mb-2">Workflow Orchestration Layer</h3>
                            <p class="text-theme-dark font-medium mb-2">Process mapping, automation routing, system integrations, event triggers, operational ownership.</p>
                            <p class="text-slate-600">This layer determines how work flows through the organization.</p>
                        </div>
                    </div>
                </div>

                <!-- Layer 2: Data Architecture -->
                <div class="sketch-card border-sketch-3 p-8 relative z-10 bg-theme-card ml-8 md:ml-16 transform transition-transform hover:-translate-y-1">
                    <div class="absolute -left-12 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-slate-500 border-4 border-theme-card flex items-center justify-center text-white font-bold text-sm shadow-sm">2</div>
                    <div class="flex flex-col md:flex-row items-start gap-4">
                        <div class="text-3xl text-slate-500 mt-1"><i class="fas fa-database"></i></div>
                        <div>
                            <h3 class="text-2xl font-bold text-theme-dark mb-2">Data Architecture Layer</h3>
                            <p class="text-theme-dark font-medium mb-2">Data normalization, contextual tagging, governance, structured storage, access controls.</p>
                            <p class="text-slate-600">Fragmented data becomes structured signal.</p>
                        </div>
                    </div>
                </div>

                <!-- Layer 1: Infrastructure -->
                <div class="sketch-card border-sketch-2 p-8 relative z-10 bg-slate-100 ml-8 md:ml-16 transform transition-transform hover:-translate-y-1">
                    <div class="absolute -left-12 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-slate-400 border-4 border-theme-card flex items-center justify-center text-white font-bold text-sm shadow-sm">1</div>
                    <div class="flex flex-col md:flex-row items-start gap-4">
                        <div class="text-3xl text-slate-400 mt-1"><i class="fas fa-server"></i></div>
                        <div>
                            <h3 class="text-2xl font-bold text-theme-dark mb-2">Infrastructure Layer</h3>
                            <p class="text-theme-dark font-medium mb-2">Endpoints, cloud environments, identity management, cybersecurity, system stability.</p>
                            <p class="text-slate-600">This layer ensures reliability and secure access.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="max-w-3xl mx-auto text-center font-hand text-xl md:text-2xl text-theme-dark font-bold leading-relaxed space-y-2">
                <p>Infrastructure supports data.</p>
                <p>Data supports workflow.</p>
                <p>Workflow enables intelligence.</p>
                <p class="text-theme-blue mt-4 text-2xl md:text-3xl transform -rotate-1">Intelligence improves performance.</p>
            </div>
        </div>
    </section>

    <!-- SECTION 2: PERFORMANCE FRAMEWORK -->
    <section class="py-20 border-t border-slate-200 bg-dot-grid">
        <div class="max-w-7xl mx-auto px-4">
            <div class="text-center mb-16">
                 <span class="inline-block font-hand text-theme-red text-xl font-bold mb-4 transform -rotate-2">
                    <i class="fas fa-tachometer-alt"></i> Performance
                </span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-theme-dark mb-6">The Five-Domain Performance Framework</h2>
                <p class="text-lg text-slate-600 max-w-3xl mx-auto">
                    A Managed Intelligence Provider validates impact through structured performance domains.
                </p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Velocity -->
                <div class="sketch-card border-sketch-1 bg-theme-card p-6 rounded-xl transition-all">
                    <div class="flex items-center gap-3 mb-4 border-b-2 border-slate-100 pb-4">
                        <span class="w-10 h-10 rounded-full bg-blue-100 text-theme-blue flex items-center justify-center text-xl"><i class="fas fa-bolt"></i></span>
                        <h3 class="text-xl font-bold text-theme-dark">Velocity</h3>
                    </div>
                    <p class="text-slate-600 font-medium">Reduced cycle time across onboarding, approvals, and production workflows.</p>
                </div>
                <!-- Cost Efficiency -->
                <div class="sketch-card border-sketch-3 bg-theme-card p-6 rounded-xl transition-all">
                    <div class="flex items-center gap-3 mb-4 border-b-2 border-slate-100 pb-4">
                        <span class="w-10 h-10 rounded-full bg-green-100 text-green-600 flex items-center justify-center text-xl"><i class="fas fa-chart-line"></i></span>
                        <h3 class="text-xl font-bold text-theme-dark">Cost Efficiency</h3>
                    </div>
                    <p class="text-slate-600 font-medium">Lowered operational overhead through automation and redesign.</p>
                </div>
                <!-- Decision Quality -->
                <div class="sketch-card border-sketch-4 bg-theme-card p-6 rounded-xl transition-all">
                    <div class="flex items-center gap-3 mb-4 border-b-2 border-slate-100 pb-4">
                        <span class="w-10 h-10 rounded-full bg-purple-100 text-purple-600 flex items-center justify-center text-xl"><i class="fas fa-balance-scale"></i></span>
                        <h3 class="text-xl font-bold text-theme-dark">Decision Quality</h3>
                    </div>
                    <p class="text-slate-600 font-medium">Improved accuracy and speed of business decisions through contextual data.</p>
                </div>
                <!-- Experience Optimization -->
                <div class="sketch-card border-sketch-5 bg-theme-card p-6 rounded-xl transition-all">
                    <div class="flex items-center gap-3 mb-4 border-b-2 border-slate-100 pb-4">
                        <span class="w-10 h-10 rounded-full bg-amber-100 text-amber-600 flex items-center justify-center text-xl"><i class="fas fa-user-friends"></i></span>
                        <h3 class="text-xl font-bold text-theme-dark">Experience Optimization</h3>
                    </div>
                    <p class="text-slate-600 font-medium">Reduced friction for employees and clients interacting with systems.</p>
                </div>
                <!-- Visibility -->
                <div class="sketch-card border-sketch-2 bg-theme-card p-6 rounded-xl transition-all">
                    <div class="flex items-center gap-3 mb-4 border-b-2 border-slate-100 pb-4">
                        <span class="w-10 h-10 rounded-full bg-indigo-100 text-indigo-600 flex items-center justify-center text-xl"><i class="fas fa-eye"></i></span>
                        <h3 class="text-xl font-bold text-theme-dark">Visibility</h3>
                    </div>
                    <p class="text-slate-600 font-medium">Real-time operational and financial insight for leadership.</p>
                </div>
            </div>

            <div class="mt-16 text-center">
                <div class="inline-block bg-theme-blue/10 border border-theme-blue px-8 py-4 rounded-xl transform rotate-1 shadow-sm">
                    <p class="text-xl font-bold text-theme-dark">
                        Intelligence is measured through <span class="marker-highlight px-2 -rotate-1 inline-block">operational improvement</span>, not tool adoption.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 3: WORKFLOW TARGETING MODEL -->
    <section class="py-20 border-t border-slate-200 bg-theme-card">
        <div class="max-w-7xl mx-auto px-4">
            <div class="grid lg:grid-cols-2 gap-16 items-center">
                <div>
                     <h2 class="text-3xl md:text-4xl font-extrabold text-theme-dark mb-6">Where Intelligence Creates Leverage</h2>
                     <p class="text-xl text-slate-600 mb-8 leading-relaxed">
                         A MIP applies intelligence selectively using structured criteria.
                     </p>
                     
                     <div class="prose text-slate-600 text-lg space-y-4">
                        <p class="font-medium">Workflows that meet these conditions produce measurable gains when structured and automated correctly.</p>
                        <p class="font-bold text-theme-dark mt-6 border-l-4 border-theme-red pl-4 py-2">
                             Intelligence is deployed after architecture and process clarity are established.
                        </p>
                     </div>
                </div>
                
                <div class="relative">
                    <div class="sticky-note p-8 md:p-10 transform rotate-1">
                        <h3 class="font-hand font-bold text-2xl text-theme-dark mb-6 hand-underline-red pb-2 inline-block">Target Criteria</h3>
                        <ul class="space-y-5 font-bold text-xl text-theme-dark">
                            <li class="flex items-center gap-4"><span class="w-8 h-8 rounded-full bg-theme-blue flex items-center justify-center text-sm"><i class="fas fa-check text-white"></i></span> High-volume</li>
                            <li class="flex items-center gap-4"><span class="w-8 h-8 rounded-full bg-theme-blue flex items-center justify-center text-sm"><i class="fas fa-check text-white"></i></span> Decision-intensive</li>
                            <li class="flex items-center gap-4"><span class="w-8 h-8 rounded-full bg-theme-blue flex items-center justify-center text-sm"><i class="fas fa-check text-white"></i></span> Repetitive</li>
                            <li class="flex items-center gap-4"><span class="w-8 h-8 rounded-full bg-theme-blue flex items-center justify-center text-sm"><i class="fas fa-check text-white"></i></span> Time-sensitive</li>
                            <li class="flex items-center gap-4"><span class="w-8 h-8 rounded-full bg-theme-blue flex items-center justify-center text-sm"><i class="fas fa-check text-white"></i></span> Data-rich</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 4: CAPABILITY MATURITY MODEL -->
    <section class="py-20 border-t border-slate-200 bg-dot-grid">
        <div class="max-w-7xl mx-auto px-4">
            <div class="text-center mb-16">
                 <h2 class="text-3xl md:text-4xl font-extrabold text-theme-dark mb-6">Capability Is Built in Stages</h2>
                 <p class="text-lg text-slate-600 max-w-3xl mx-auto">
                     Becoming a Managed Intelligence Provider is a structured progression.
                 </p>
            </div>

            <!-- Graphic representation: Staircase -->
            <div class="max-w-6xl mx-auto mb-16 relative">
                <div class="grid grid-cols-1 lg:grid-cols-5 gap-4 h-full relative z-10 items-end">
                    
                    <!-- Stage 1 -->
                    <div class="flex flex-col text-center group">
                        <div class="p-6 bg-slate-100 sketch-card border-sketch-3 rounded-t-xl min-h-[140px] transform transition-transform group-hover:-translate-y-2 relative">
                            <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-theme-card border border-slate-200 font-bold text-xs uppercase px-3 py-1 rounded-full whitespace-nowrap text-slate-500">Stage 1</div>
                            <h3 class="font-bold text-theme-dark text-lg mb-2 leading-tight mt-2">Reactive<br>Infrastructure<br>Provider</h3>
                            <p class="text-sm font-medium text-slate-600">Infrastructure management and ticket-driven workflows.</p>
                        </div>
                    </div>

                    <!-- Stage 2 -->
                    <div class="flex flex-col text-center group">
                        <div class="p-6 bg-slate-200 sketch-card border-sketch-2 rounded-t-xl min-h-[180px] transform transition-transform group-hover:-translate-y-2 lg:-mb-10 lg:bottom-10 relative">
                             <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-theme-card border border-slate-300 font-bold text-xs uppercase px-3 py-1 rounded-full whitespace-nowrap text-slate-600">Stage 2</div>
                            <h3 class="font-bold text-theme-dark text-lg mb-2 leading-tight mt-2">Structured<br>MSP</h3>
                             <p class="text-sm font-medium text-slate-600">Process standardization and internal automation improvements.</p>
                        </div>
                    </div>

                    <!-- Stage 3 -->
                    <div class="flex flex-col text-center group">
                        <div class="p-6 bg-blue-50 sketch-card border-sketch-4 rounded-t-xl min-h-[220px] transform transition-transform group-hover:-translate-y-2 lg:-mb-20 lg:bottom-20 relative">
                             <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-theme-card border border-blue-200 font-bold text-theme-blue text-xs uppercase px-3 py-1 rounded-full whitespace-nowrap">Stage 3</div>
                            <h3 class="font-bold text-theme-dark text-lg mb-2 leading-tight mt-2">Data-Aware<br>Provider</h3>
                             <p class="text-sm font-medium text-slate-600">Cross-platform reporting and operational visibility.</p>
                        </div>
                    </div>

                    <!-- Stage 4 -->
                    <div class="flex flex-col text-center group">
                        <div class="p-6 bg-theme-blue/10 sketch-card border-sketch-1 rounded-t-xl min-h-[260px] transform transition-transform group-hover:-translate-y-2 lg:-mb-30 lg:bottom-30 relative">
                            <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-theme-card border border-theme-blue font-bold text-theme-blue text-xs uppercase px-3 py-1 rounded-full whitespace-nowrap">Stage 4</div>
                            <h3 class="font-bold text-theme-dark text-lg mb-2 leading-tight mt-2">Workflow-Oriented<br>Intelligence Provider</h3>
                            <p class="text-sm font-medium text-slate-600">Process mapping and targeted automation within client workflows.</p>
                        </div>
                    </div>

                    <!-- Stage 5 -->
                    <div class="flex flex-col text-center group">
                            <div class="p-6 bg-theme-blue sketch-card border-sketch-5 rounded-t-xl min-h-[300px] transform transition-transform group-hover:-translate-y-2 lg:-mb-40 lg:bottom-40 relative">
                                <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-theme-card border-2 border-theme-blue font-black text-theme-dark text-xs uppercase px-3 py-1 rounded-full whitespace-nowrap shadow-sm">Stage 5</div>
                                <h3 class="font-bold text-white text-xl mb-4 leading-tight mt-2">Managed<br>Intelligence<br>Provider</h3>
                                <p class="text-sm font-medium text-blue-50">Integrated architecture, intelligence embedded in high-leverage systems, measurable performance gains.</p>
                            </div>
                    </div>

                </div>
                <!-- Foundation line -->
                <div class="h-3 bg-slate-200 rounded-full w-full mt-4 z-0 hidden lg:block mb-8"></div>
            </div>

            <div class="max-w-3xl mx-auto text-center mt-12 lg:mt-32">
                 <p class="text-xl text-theme-dark font-extrabold mb-6">Each stage builds on the one beneath it.</p>
                 <div class="inline-flex flex-col items-center gap-3 font-hand text-xl text-slate-600 bg-white border border-slate-200 px-8 py-6 rounded-xl rotate-1 shadow-sm">
                    <div class="flex items-center gap-2">Infrastructure maturity <i class="fas fa-arrow-right text-base text-slate-400"></i> data maturity.</div>
                    <div class="flex items-center gap-2">Data maturity <i class="fas fa-arrow-right text-base text-slate-400"></i> workflow clarity.</div>
                    <div class="flex items-center gap-2 text-theme-blue text-2xl font-black mt-2">Workflow clarity <i class="fas fa-arrow-right text-base text-theme-dark"></i> intelligence.</div>
                 </div>
            </div>
        </div>
    </section>

    <!-- SECTION 5: POSITIONING SHIFT -->
    <section class="py-20 border-t border-slate-200 bg-theme-card">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <h2 class="text-3xl md:text-4xl font-extrabold text-theme-dark mb-6">From System Maintenance to Operational Engineering</h2>
            <p class="text-xl text-slate-600 mb-12">
                The transition from MSP to MIP changes engagement scope.
            </p>

            <div class="sketch-card border-sketch-3 bg-white p-10 mb-10 text-center mx-auto max-w-3xl">
                <div class="grid md:grid-cols-2 gap-8 text-left text-lg">
                    <div class="space-y-6 flex flex-col justify-center">
                        <div class="flex items-center text-slate-400 gap-4 line-through">
                             <i class="fas fa-layer-group opacity-50 w-6"></i> Tool Stacks
                        </div>
                        <div class="flex items-center text-slate-400 gap-4 line-through">
                             <i class="fas fa-server opacity-50 w-6"></i> Uptime
                        </div>
                        <div class="flex items-center text-slate-400 gap-4 line-through">
                             <i class="fas fa-file-signature opacity-50 w-6"></i> Service Contracts
                        </div>
                    </div>

                    <div class="space-y-6 md:border-l-2 border-slate-100 md:pl-10">
                        <div class="flex items-center text-theme-dark font-bold gap-4">
                             <i class="fas fa-chart-bar text-theme-blue w-6 text-xl"></i> Metrics
                        </div>
                        <div class="flex items-center text-theme-dark font-bold gap-4">
                             <i class="fas fa-balance-scale-right text-theme-blue w-6 text-xl"></i> Operational Leverage
                        </div>
                        <div class="flex items-center text-theme-dark font-bold gap-4">
                             <i class="fas fa-rocket text-theme-blue w-6 text-xl"></i> Performance Initiatives
                        </div>
                    </div>
                </div>
            </div>

            <p class="text-xl font-bold text-theme-dark max-w-2xl mx-auto">
                <span class="marker-highlight px-2">This shift increases strategic relevance</span> and long-term client alignment.
            </p>
        </div>
    </section>

    <!-- SECTION 6: MARKET CONDITIONS -->
    <section class="py-20 border-t border-slate-200 bg-dot-grid">
        <div class="max-w-7xl mx-auto px-4">
            <div class="grid md:grid-cols-2 gap-16 items-center">
                <div class="order-2 md:order-1 relative">
                    <div class="w-72 h-72 mx-auto border-4 border-white sketch-card border-sketch-5 flex items-center justify-center bg-theme-blue transform -rotate-3 text-white">
                        <div class="text-center p-6">
                            <i class="fas fa-globe text-6xl mb-6"></i>
                            <div class="font-hand font-bold text-3xl leading-tight">The Time<br>Is Now</div>
                        </div>
                    </div>
                </div>

                <div class="order-1 md:order-2">
                    <span class="inline-block font-hand text-theme-red text-xl font-bold mb-4 transform -rotate-1">
                        <i class="fas fa-chart-network"></i> Market Reality
                    </span>
                    <h2 class="text-3xl md:text-4xl font-extrabold text-theme-dark mb-8">The Conditions Are Already Present</h2>
                    
                    <ul class="space-y-8 text-xl text-slate-600 mb-10">
                        <li class="flex items-start gap-4">
                            <i class="fas fa-robot text-theme-blue mt-1"></i>
                            <span><strong class="text-theme-dark">Automation tooling</strong> is accelerating.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <i class="fas fa-brain text-theme-blue mt-1"></i>
                            <span><strong class="text-theme-dark">AI capability</strong> is expanding.</span>
                        </li>
                        <li class="flex items-start gap-4">
                            <i class="fas fa-search-dollar text-theme-blue mt-1"></i>
                            <span>Clients are evaluating <strong class="text-theme-dark">operational efficiency</strong> at increasing frequency.</span>
                        </li>
                    </ul>

                    <div class="p-6 bg-white sketch-card border-sketch-4">
                        <p class="font-bold text-xl text-theme-dark mb-3">The market is ready for intelligence-driven service models.</p>
                        <p class="font-bold text-lg text-theme-blue">The differentiator is architectural discipline.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 7: CLOSE -->
    <section class="py-32 border-t border-slate-200 bg-theme-dark text-white text-center">
        <div class="max-w-4xl mx-auto px-4 relative z-10">
            <h2 class="text-5xl md:text-7xl font-black mb-8 leading-tight">Managed Intelligence Provider</h2>
            
            <div class="flex flex-wrap justify-center gap-4 text-2xl md:text-3xl font-hand font-bold text-slate-300 mb-12">
                <span class="text-white hover:-translate-y-1 transition-transform cursor-default">Architecture.</span>
                <span class="text-white hover:-translate-y-1 transition-transform cursor-default">Workflow.</span>
                <span class="text-white hover:-translate-y-1 transition-transform cursor-default">Intelligence.</span>
                <span class="text-theme-blue hover:-translate-y-1 transition-transform cursor-default">Performance.</span>
            </div>

            <p class="text-2xl md:text-3xl font-medium text-slate-300 mb-16 max-w-2xl mx-auto">
                The next phase of the industry has a <span class="text-white border-b-2 border-theme-blue pb-1">defined model.</span>
            </p>

            <div class="flex flex-col sm:flex-row items-center justify-center gap-8">
                <!-- Primary Button (Using standard blue button) -->
                <a href="/join.html" class="sketch-button-blue px-10 py-5 text-xl font-bold flex items-center gap-3">
                    Enter the Guild <i class="fas fa-arrow-right"></i>
                </a>
                
                <!-- Secondary Link -->
                <a href="/guild.html" class="font-bold text-xl text-slate-300 hover:text-white transition-colors underline decoration-2 underline-offset-8 decoration-theme-blue hover:decoration-white">
                    Explore the Guild Experience
                </a>
            </div>
        </div>
    </section>
"""
import re
pattern = re.compile(r'    <!-- HERO SECTION -->.*?    <!-- FOOTER -->', re.DOTALL)
new_content = pattern.sub(new_html + "    <!-- FOOTER -->", html)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)
print("done")
