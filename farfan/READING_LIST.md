# Reading list: neural coding to neurotechnology

Read in order. “Major result” reports the cited work’s result, not a conclusion that this repository has independently reproduced it.

Citation identities and summaries audited on 2026-10-01; see [source audit](SOURCE_AUDIT.md) for corrections and access limitations. All six papers include Fernando D./Daniel Farfán as an author.

## 1. Local tactile-sensing foundations

### Albarracín et al. (2006), *Texture discrimination and multi-unit recording in the rat vibrissal nerve*

- **Source:** [BMC Neuroscience / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1525197/), DOI: [10.1186/1471-2202-7-42](https://doi.org/10.1186/1471-2202-7-42)
- **Question:** Does multi-fiber vibrissal-nerve activity contain information that differentiates textures during active touch, and does pressure matter?
- **System/data:** anesthetized rats; multifiber activity from a deep vibrissal nerve during artificial whisking induced by facial-nerve electrical stimulation across materials. This was not freely behaving texture discrimination.
- **Method:** RMS, PSD, controls, and statistical comparisons.
- **Major result:** response amplitude/frequency features varied with stimulus/pressure conditions; the authors interpret pressure as a possible information-acquisition strategy.
- **Why read it:** It grounds “neural coding” in an actual measurement chain rather than a slogan.
- **Prerequisites:** sensory transduction, afferent activity, RMS/PSD, experimental controls, and the limits of multi-unit recording.

### Dürig et al. (2009), *Design and construction of a photoresistive sensor for monitoring the rat vibrissal displacement*

- **Source:** [PubMed](https://pubmed.ncbi.nlm.nih.gov/19427531/), DOI: [10.1016/j.jneumeth.2009.02.020](https://doi.org/10.1016/j.jneumeth.2009.02.020)
- **Question:** Can a simple instrument reliably measure individual vibrissal motion?
- **System/data:** physical whisker displacement measured with an LED/LDR device.
- **Method:** instrument design, transduction from shadow to resistance/voltage, validation of movement tracking.
- **Major result:** the sensor tracked single-vibrissa horizontal displacement.
- **Why read it:** Neural coding begins before spikes: stimulus measurement and instrumentation determine what a later analysis can claim.
- **Prerequisites:** sensors, voltage/resistance, measurement error, calibration.

### Farfán, Albarracín & Felice (2013), *Neural encoding schemes of tactile information in afferent activity of the vibrissal system*

- **Source:** [PubMed](https://pubmed.ncbi.nlm.nih.gov/22723154/), DOI: [10.1007/s10827-012-0408-6](https://doi.org/10.1007/s10827-012-0408-6)
- **Date:** journal issue February 2013; first published online in June 2012. Both years can appear in databases.
- **Question:** Which event-based descriptions of vibrissal afferent activity carry texture-related information?
- **System/data:** rat vibrissal afferent recordings during tactile sweeps.
- **Method:** continuous-wavelet event detection; cumulative event count and median inter-event time; Shannon mutual information.
- **Major result:** particular event durations/codes carried discriminative information, and extreme snout–surface distance reduced information values.
- **Why read it:** This is the closest direct bridge to Module 03: rate-like counts, temporal intervals, event definition, and information measurement.
- **Prerequisites:** spike/event trains, time–frequency methods, entropy, mutual information, estimator bias, encoding versus decoding.

### Alegre-Cortés et al. (2018), *Toward an Improvement of the Analysis of Neural Coding*

- **Source:** [Frontiers in Neuroinformatics](https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2017.00077/full) / [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5767721/), DOI: [10.3389/fninf.2017.00077](https://doi.org/10.3389/fninf.2017.00077)
- **Article type/date:** Perspective, published 10 January 2018 in volume 11 (2017), article 77.
- **Question:** How can signal decomposition and information-based analysis improve neural-coding analysis?
- **System/data:** includes rat vibrissal-nerve texture recordings as a motivating example.
- **Method:** noise-assisted multivariate empirical mode decomposition (NA-MEMD), time–frequency features, multilayer-perceptron classification, shuffled-label comparisons, and t-SNE visualization.
- **Major result:** argues that analysis representation can materially affect what coding evidence is recovered.
- **Why read it:** A warning that “the code” is partly a measurement/modeling question; do not choose representations after looking for favorable results.
- **Prerequisites:** time–frequency analysis, classification, validation, dimensionality reduction, and multiple comparisons.

## 2. Neural interfaces, stability, and adaptation

### Grani et al. (2022), *Time stability and connectivity analysis with an intracortical 96-channel microelectrode array inserted in human visual cortex*

- **Source:** [PubMed](https://pubmed.ncbi.nlm.nih.gov/35817011/), DOI: [10.1088/1741-2552/ac801d](https://doi.org/10.1088/1741-2552/ac801d)
- **Question:** How stable are signals/connectivity measures from a chronically implanted visual-cortex array, and how are they altered around stimulation?
- **System/data:** a 96-channel intracortical array in one blind volunteer, measured over six months.
- **Method:** variance, PSD, correlation, coherence, and phase coherence before/after stimulation.
- **Major result:** variance/PSD showed no significant trend over six months, whereas several connectivity measures changed; the authors discuss possible plasticity-related interpretations cautiously.
- **Why read it:** It introduces a real longitudinal neural-interface stability problem and the difference between signal features and connectivity metrics.
- **Prerequisites:** implanted recordings, PSD, correlation/coherence, longitudinal design, n=1 limitations.

### Farfán et al. (2025), *Brain connectivity changes in response to cortical electrical stimulation in blind neuroprosthesis users*

- **Source:** [PubMed](https://pubmed.ncbi.nlm.nih.gov/40173310/) · [Cerebral Cortex](https://academic.oup.com/cercor/article/35/4/bhaf075/8104078), DOI: [10.1093/cercor/bhaf075](https://doi.org/10.1093/cercor/bhaf075)
- **Question:** How do resting-state cortical connectivity patterns change during use of a cortical visual prosthesis?
- **System/data:** resting-state scalp EEG from two blind participants with intracortical visual implants, followed over six months.
- **Method:** spectral coherence across 64 EEG channels. The implant delivered cortical stimulation; the connectivity analysis used scalp EEG.
- **Major result:** the paper reports changes in selected connectivity patterns and frames them as evidence consistent with adaptive cortical-network change; it explicitly calls for more study.
- **Why read it:** It connects neurotechnology to longitudinal neural dynamics while showing why a connectivity change is not automatically a causal or clinical-success mechanism.
- **Prerequisites:** EEG preprocessing, spectral coherence, frequency bands, longitudinal inference, a two-participant study's limitations, and cautious causal language.

## How to take notes

For every paper, answer: What is the physical stimulus/task? What was measured? What transformation creates the response variable? What quantity is called “information” or “connectivity”? What is the observational unit? What alternative explanation remains? Then map one unknown concept to `ROADMAP.md`.
