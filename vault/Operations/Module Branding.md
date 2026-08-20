---
type: notion-import
notion-id: 38c8924af01480daa758dd99aa623305
source-url: https://app.notion.com/p/lewagon/Module-Branding-38c8924af01480daa758dd99aa623305
imported: 2026-07-23
---
# Module Branding
## **Design Overview**
### **Layout Structure**
- **Header section** with label, title, description, and "Download Syllabus PDF" button (outline style)
- **7 expandable accordion modules** (max-width: 1024px, centered)
- **Collapsed state**: Module number badge, category label, module title, and plus icon
- **Expanded state**: Module description + "What You'll Build" checklist (full width)
- **Single-open accordion**: Only one module can be expanded at a time
### **Typography System**
- **CircularStd-Bold**: Label, title, button, module categories, module titles, section headings
- **Inter**: Description text, module descriptions, checklist items
### **Color Palette**
- **White Background**: #ffffff (section + cards)
- **Primary Purple**: #4d04c4 (label, category text, icons, active number badge)
- **Light Purple**: #EEE8FF (active accordion background, button hover)
- **Gray Border**: #E5E7EB (card borders, collapsed number badge background)
- **Muted Gray**: #9CA3AF (collapsed number badge text)
- **Dark Text**: #1A1A1A (titles, headings)
- **Gray Text**: #4B5563 (descriptions, checklist items)
### **Interactive Behavior**
- **Click to expand**: Module opens and all others close automatically
- **Icon toggle**: Plus icon → Minus icon when expanded
- **Active state**: Purple background (#EEE8FF) + purple number badge
- **Hover effect**: Semi-transparent purple background on module header
### **Color Palette**
Color NameHex CodeUsagePrimary Purple#4d04c4Buttons, links, icons, highlightsPurple Hover#3a0396Button hover statesLight Purple#EEE8FFIcon backgrounds, button hoverDark Purple#371373Who section backgroundPurple Gradient Start#6D28D9Career stat card gradientDark Text#1A1A1AHeadlines, titlesGray Text#4B5563Body copy, descriptionsMuted Gray#9CA3AFSecondary text, muted titlesLight Gray#848a94Trust badge, prerequisitesBackground Peach#FFF7EDProblem section backgroundBackground Gray#F9FAFBCareer section backgroundBorder Gray#E5E7EBCard borders, dividersWhite#ffffffPrimary background, cards
### **Section Label Standard**
All section labels follow this pattern:
```
.section-label{display:inline-block!important;font-size:0.75rem!important;font-weight:900!important;text-transform:uppercase!important;letter-spacing:0.05em!important;color:#4d04c4!important;background-color:transparent!important;padding:0.5rem 1rem!important;border-radius:9999px!important;margin-bottom:1.5rem!important;font-family:"CircularStd-Bold","CircularStd-Medium","Helvetica",sans-serif!important;}​
```
**Key Properties:**
- Font weight: **900** (not 700)
- Letter spacing: **0.05em** (not 0.1em)
- Background: **transparent** (no background color)
- Always uppercase
- Always CircularStd-Bold
### **Spacing System**
SizeValueUsageXS0.5rem (8px)Icon gaps, tight spacingSM1rem (16px)Card gaps, list spacingMD1.5rem (24px)Element spacingLG2rem (32px)Section spacingXL3rem (48px)Major section gaps2XL4rem (64px)Section margins3XL6rem (96px)Section padding top/bottom
### **Breakpoints**
NameSizeUsageMobile< 640pxSingle column, stacked layoutTablet640px - 767pxSome horizontal layoutsDesktop≥ 768pxFull layout, multi-column gridsLarge Desktop≥ 1024pxHero section two-column
css code landing page
```
@font-face {
  font-family: CircularStd-Black;
  src: url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Black.eot") format("embedded-opentype"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Black.woff") format("woff"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Black.woff2") format("woff2"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Black.ttf") format("truetype");
}
@font-face {
  font-family: CircularStd-Bold;
  src: url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Bold.eot") format("embedded-opentype"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Bold.woff") format("woff"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Bold.woff2") format("woff2"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Bold.ttf") format("truetype");
}
@font-face {
  font-family: Graphik-Regular;
  src: url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/Graphik-Regular.eot") format("embedded-opentype"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/Graphik-Regular.woff") format("woff"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/Graphik-Regular.ttf") format("truetype");
}
@font-face {
  font-family: Graphik-Medium;
  src: url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/Graphik-Medium.eot") format("embedded-opentype"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/Graphik-Medium.woff") format("woff"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/Graphik-Medium.ttf") format("truetype");
}
@font-face {
  font-family: Graphik-Light;
  src: url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/Graphik-Light.eot") format("embedded-opentype"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/Graphik-Light.woff") format("woff"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/Graphik-Light.ttf") format("truetype");
}
:root {
  /* PRIMARY COLORS */
  --red: #FD1015;
  --hovered-red: #e45d60;
  --dark-red: #C40004;
  --light-red: #FEE0E0;
  --black: #0E0000;
  --dark-grey: #4A4A4A;
  --light-black: #4b4b4b;
  --grey: #d5d5d5;
  --light-grey: #EAEAEA;
  --cream: #FCF5E8;
  --purple: #7971FB;
  --light-purple: #EBE9FE;
  --blue: #62DDF5;
  --light-blue: #E8FAFE;
  --dark-blue: #1db2ff;
  --green: #1EDD88;
  --light-green: #E4FFF3;
  --yellow: #FFC65A;
  --light-yellow: #FFF7E8;
  --indigo: #7E73FF;
  --light-indigo: #ECEAFF;
  --purple-openclassroom: #7451eb;
  --light-purple-openclassroom: #9C76F8;
  /* FONT-SIZE */
  --main-title: 48px;
  --large-title: 40px;
  --medium-title: 30px;
  --small-title: 24px;
  --large-paragraph: 21px;
  --medium-paragraph: 18px;
  --small-paragraph: 15px;
  --extra-small-paragraph: 14px;
  /* EFFECTS */
  --box-shadow: 0 15px 35px rgba(126, 87, 88, 0.1), 0 5px 15px rgba(0,0,0,.07);
  --button-shadow: 0 2px 14px rgba(126,87,88,.1),0 3px 6px rgba(0,0,0,.08);
}
*, *:before, *:after {
  -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box;
}
html, body {
  min-height: 100%;
  margin: 0;
  padding: 0;
  scroll-behavior: smooth;
}
body {
  box-sizing: border-box;
  font-family: Graphik-Regular,SimHei;
  letter-spacing: .1px;
  color: var(--light-black);
  font-size: 1em;
  line-height: 1.6em;
}
/* Page Center */
.container-fluid .row-fluid .page-center {
  float: none;
  max-width: 1170px;
  margin: 0 auto;
  padding-left: 15px;
  padding-right: 15px;
}
/* Highlighted Text */
::-moz-selection {
  color: #fff;
  background: #328EFA;
  text-shadow: none;
}
::selection {
  color: #fff;
  background: #328EFA;
  text-shadow: none;
}
div#site-wrapper {
  margin: 0 auto;
}
/* =============== Typography =============== */
/* Anchor Links */
a {
  color: var(--red);
  text-decoration: none;
}
a:hover, a:focus, a:active {
  text-decoration: underline;
}
/* Basic text */
h1, h2, h3, h4 {
  margin-top:0px;
  margin-bottom:20px;
  letter-spacing: .1px;
  font-family: CircularStd-Black, SimHei;
  color: var(--black);
}
h1 {
  line-height: 1.2em;
  font-size: var(--main-title);
}
h2 {
  line-height: 1.35em;
  font-size: var(--large-title);
}
h3 {
  line-height: 1em;
  font-size: var(--medium-title);
}
h4 {
  line-height: 1em;
  font-size: var(--small-title);
}
p, li {
  color: var(--light-black);
  font-size: var(--small-paragraph);
}
ul {
  margin: 0 0 20px;
  padding: 8px 0 0 16px;
}
ul li::marker {
  color: var(--red);
}
strong {
  font-family: Graphik-Medium;
  font-weight: 100;
}
blockquote {
  position: relative;
  margin: 16px 0 30px;
  font-size: var(--large-paragraph);
  font-style: italic;
}
figcaption {
  position: absolute;
  bottom: -26px;
  font-size: var(--extra-small-paragraph);
  left: 0;
}
button {
  appearance: none;
  background-color: transparent;
  border: none;
}
pre {
  padding: 6px 12px 4px;
  color: var(--black);
  background-color: var(--light-grey);
  border: 1px solid var(--grey);
  border-radius: 6px;
  hyphens: none;
  white-space: pre-wrap;
  word-wrap: break-word;
  word-wrap: break-word;
  overflow-wrap: break-word;
  line-break: strict;
}
img {
  margin-bottom: 20px;
  max-width: 100%;
  height: auto;
}
sup, sub {
  position: relative;
  font-size: 75%;
  line-height: 0;
  vertical-align: baseline;
}
sup { top: -0.5em; }
sub { bottom: -0.25em; }
::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  font-size: var(--extra-small-paragraph);
  font-family: Graphik-Regular;
}
:-ms-input-placeholder { /* Internet Explorer 10-11 */
  font-size: var(--extra-small-paragraph);
  font-family: Graphik-Regular;
}
::-ms-input-placeholder { /* Microsoft Edge */
  font-size: var(--extra-small-paragraph);
  font-family: Graphik-Regular;
}
/* =============== Title highlighted effect =============== */
.highlighted {
  padding: 2px 15px 4px;
  font-style: normal;
  font-family: var(--circular-black);
  border-radius: 3px;
}
.highlighted-red {
  color: var(--red);
  background: var(--light-red);
}
.highlighted-blue {
  color: var(--blue);
  background: var(--light-blue);
}
.highlighted-green {
  color: var(--green);
  background: var(--light-green);
}
.highlighted-yellow {
  color: var(--yellow);
  background: var(--light-yellow);
}
.highlighted-purple {
  color: var(--purple);
  background: var(--light-purple);
}
@-moz-document url-prefix() {
  .highlighted {
    padding: 7px 15px 6px;
  }
}
/* =============== Layout classes =============== */
body.landing-body {
  overflow-x: hidden;
}
.landing-main-wrapper {
  max-width: 980px !important;
  margin: 0 auto !important;
  float: none !important;
}
.landing-content-container {
  padding-right: 22px;
}
@media (max-width: 767px) {
  .landing-content-container {
    padding-right: 0;
  }
}
.landing-newsletter-wrapper {
  position: relative
}
.landing-newsletter-wrapper:after {
  content: url('https://f.hubspotusercontent10.net/hubfs/4419217/landing_images/landing-newsletter-illustration.svg');
  position: absolute;
  bottom: -250px;
  left: 50%;
  transform: translateX(-50%);
  z-index: -1;
}
@media (max-width: 1020px) {
  .landing-main-wrapper {
    padding: 0 20px;
    overflow: hidden;
  }
}
.landing-section {
  padding: 60px 0;
}
.landing-section.no-padding {
  padding: 0 0 60px 0;
  margin-top: -60px;
}
.landing-fullpage .landing-section-ivory,
.landing-one-column .landing-section-ivory,
.landing-two-columns .landing-section-ivory {
  position: relative;
}
.landing-fullpage .landing-section-ivory::after {
  content: '';
  position: absolute;
  width: 100vw;
  height: 100%;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  background-color: var(--cream);
  z-index: -1;
}
.landing-one-column .landing-section-ivory::after {
  content: '';
  position: absolute;
  position: absolute;
  width: 100vw;
  height: 100%;
  top: 0;
  left: calc((100vw - 61rem)/2);
  transform: translateX(calc((-100vw + 61rem)));
  background-color: var(--cream);
  z-index: -1;
}
@media(max-width:  1024px) {
  .landing-one-column .landing-section-ivory::after {
    transform: inherit;
    left:  -20px;
  }
 }
.landing-two-columns .landing-section-ivory::after {
  content: '';
  position: absolute;
  width: 100vw;
  height: 100%;
  top: 0;
  left: 0;
  background-color: var(--cream);
  z-index: -1;
}
/* =============== Form =============== */
.landing-form-container {
  position: sticky;
  top: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: white;
  border-radius: 6px;
  box-shadow: var(--box-shadow);
  border: 1px solid var(--grey);
  overflow: hidden;
}
.landing-form-apply {
  height: fit-content;
}
.landing-form-apply iframe {
  width: 100%;
  height: 100%;
  border: none;
}
@media (max-width: 767px) {
  .landing-form-container {
    margin-top: 0;
  }
}
.form-title {
  padding: 16px;
  margin-bottom: 0;
  font-size: var(--small-paragraph);
  font-family: Graphik-Regular;
  color: white;
  background-color: var(--black);
}
.landing-form-container form {
  padding: 16px;
}
form .primary {
  padding: 12px 26px;
  width: 100%;
  min-height: 54px;
  font-size: var(--small-paragraph);
  background-color: var(--red);
  color: white;
  border: none;
  border-radius: 3px;
  font-family: Graphik-Medium;
  box-shadow: var(--button-shadow);
}
form .primary:hover {
  cursor: pointer;
  background-color: var(--hovered-red);
}
form label {
  font-size: var(--extra-small-paragraph);
}
form legend {
  position: absolute;
  bottom: -18px;
  font-size: 10px;
  text-align: right;
}
form .field {
  position: relative;
  margin-bottom: 6px;
}
form fieldset.form-columns-1,
form fieldset.form-columns-2 {
  max-width: 100%;
}
form fieldset.form-columns-1 > label,
form fieldset.form-columns-1 > .input {
  width: 100% !important;
  margin: 0 !important;
}
form fieldset.form-columns-2 > label,
form fieldset.form-columns-2 > .input {
  width: 100% !important;
}
form fieldset.form-columns-2 .field:last-of-type .input {
  margin: 0 !important;
}
form fieldset.form-columns-1 .input {
  margin: 0 !important;
}
form fieldset.form-columns-1 .input input {
  width: 100% !important;
}
form fieldset.form-columns-1 .input .hs-form-checkbox-display input {
  margin-right: 6px;
  width: auto !important;
}
form input {
  padding: 8px 12px;
  margin: 0;
  width: 100%;
  background: #f5f5f5;
  border: 1px solid var(--grey);
  border-radius: 3px;
  font-size: var(--small-paragraph);
}
form textarea {
  padding: 12px;
  margin-bottom: 6px;
  width: 100% !important;
  min-height: 120px;
  border: 1px solid var(--grey);
  border-radius: 3px;
  font-size: var(--small-paragraph);
  resize: none;
}
form .legal-consent-container p {
  font-size: 12px;
  line-height: 0.9rem;
  opacity: 0.6;
}
form .legal-consent-container ul {
  list-style: none;
  padding: 0 !important;
}
form .legal-consent-container label {
  display: flex;
}
form .legal-consent-container input {
  position: relative;
  margin: 0 6px 0 0 !important;
  max-width: 20px;
  height: 16px;
}
form .legal-consent-container span {
  margin: 0 !important;
  line-height: 0.9rem;
}
.inputs-list {
  padding: 8px 0 0 0;
  list-style: none;
}
.hs-form-radio-display {
  display: flex;
}
.hs-form-radio-display .hs-input {
  margin-right: 6px;
  width: auto;
}
/* =============== Select =============== */
select {
  border: none;
  outline: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: 0;
  margin: 0;
  display: block;
  width: 100%;
  padding: 12px 55px 15px 15px;
  font-size: 14px;
  color: var(--black);
  background-color: var(--cream);
  width: 100% !important;
}
.hs-fieldtype-select .input:after {
  content: '';
  position: relative;
  float: right;
  width: 8px;
  height: 8px;
  top: -28px;
  right: 20px;
  border-left: 1px solid var(--black);
  border-top: 1px solid var(--black);
  transform: rotate(-135deg);
}
.submitted-message {
  padding: 20px;
}
.hs-fieldtype-intl-phone {
  display: flex;
}
.hs-fieldtype-intl-phone .hs-input {
  padding-right: 15px;
}
/* =============== Embed =============== */
.hs-responsive-embed {
  padding-bottom: 56% !important;
  margin-bottom: 30px !important;
  max-width: 100% !important;
}
/* =============== CTA =============== */
.cta {
  display: inline-block;
  position: relative;
  padding: 20px 32px;
  min-width: 190px;
  min-height: 64px;
  border-radius: 3px;
  font-weight: 700;
  color: white;
  font-family: Graphik-Medium;
  text-decoration: none;
  text-align: center;
  cursor: pointer;
}
.cta.primary {
  background-color: var(--red);
}
.cta.primary:hover,
.cta.primary:active,
.cta.primary:focus {
  cursor: pointer;
  background-color: var(--hovered-red);
  text-decoration: none;
}
.cta.secondary {
  background-color: white;
  color: var(--red);
  box-shadow: var(--box-shadow);
  transition: all 0.2s ease-in-out;
}
.cta.secondary:hover,
.cta.secondary:active,
.cta.secondary:focus {
  top: -2px;
  cursor: pointer;
  background-color: white;
  text-decoration: none;
}
.cta.openclassroom--purple {
  background-color: var(--purple-openclassroom);
}
.cta.openclassroom--purple:hover,
.cta.openclassroom--purple:active,
.cta.openclassroom--purple:focus {
  cursor: pointer;
  background-color: var(--light-purple-openclassroom);
  text-decoration: none;
}
.cta.openclassroom--white {
  background-color: white;
  color: var(--purple-openclassroom);
  border: 1px solid var(--purple-openclassroom);
}
.cta.openclassroom--white:hover,
.cta.openclassroom--white:active,
.cta.openclassroom--white:focus {
  cursor: pointer;
  background-color: var(--light-purple-openclassroom);
  color: white;
  text-decoration: none;
}
.cta-image {
  display: block;
  padding: 20px 32px;
  margin: 16px auto 0;
  width: 100%;
  text-align: center;
}
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
@font-face {
  font-family: CircularStd-Black;
  src: url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Black.eot") format("embedded-opentype"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Black.woff") format("woff"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Black.woff2") format("woff2"),
    url("//cdn2.hubspot.net/hubfs/4419217/Le_Wagon_January2019%20Header/Fonts/CircularStd-Black.ttf") format("truetype");
}
* {
  color: #394053;
  font-family: "Inter";
}
body {
  font-size: 18px;
}
@media (max-width:  576px) {
}
@media (max-width:  768px) {
  body {
    font-size: 16px;
  }
}
@media (max-width:  992px) {
}
@media (max-width:  1200px) {
}
@media (max-width:  1400px) {
}
h1, h2, h3, h4, h5, h6 {
  font-family: "CircularStd-Black";
  color:  #132145;
}
header {
  padding: 60px 0 120px;
}
.container {
  max-width: 1160px;
}
/*.w-85 {
  width: 85% !important;
}*/
.btn {
  padding: 1rem 2rem;
  border-radius: 8px;
  font-weight: 700;
}
.btn-red {
  color: white;
  background-color: #EA2D31;
}
.btn-red:hover,
.btn-red:active,
.btn-red:visited,
.btn-red:focus  {
  color: rgba(255,255,255, 0.9);
}
.highlighted-red {
  padding: 7px 15px 6px;
  border-radius: 4px;
  color: #EA2D31;
  background-color: rgba(234, 45, 49, 0.1);
  font-style: inherit;
  font-family: inherit;
  font-size: inherit;
}
.bg-red{
  background-color: $value;
}
.text-red {
  color: $value;
}
.rounded-pill.bg-red {
  color: $value;
  background: rgba($value, 0.1);
}​
```
## Related
- [[Content]]
