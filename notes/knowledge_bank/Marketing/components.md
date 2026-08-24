---
type: notion-import
notion-id: 38d8924af01480429219cedd94df1690
source-url: https://app.notion.com/p/lewagon/components-38d8924af01480429219cedd94df1690
imported: 2026-07-23
---
# components
Accordion
```
.accordion-button {
  font-family: $font-family-sans-serif;
  background-color: white !important;
  color: inherit !important;
}
.accordion-button:not(.collapsed) {
  color: inherit !important;
}
@include media-breakpoint-down(lg) {
  .accordion-button:not(.collapsed) {
    background-color: $cream !important;
  }
}
.accordion-item.bg-transparent {
  .accordion-button.bg-transparent,
  .accordion-body {
    @extend .px-0;
    @extend .bg-transparent;@include media-breakpoint-up(md) {
      padding: 1rem 1.25rem;
    }}
}
.accordion-button:focus,
.accordion-button:active {
  box-shadow: 0 0 0 white !important;
}
.accordion-mobile {
  .accordion-button:after {
    width: 10px;
    height: 6px;
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/simple-arrow-down.svg");
    background-size: auto;
  }
  .accordion-button:not(.collapsed)::after {
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/simple-arrow-down.svg");
  }
  .accordion-button:not(.collapsed) {
    @extend .fw-bold;
  }
}
.accordion-mobile-colored, .accordion-fundings {
  .accordion-button:after {
    width: 25px;
    height: 25px;
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/circle-arrow-down.svg");
    background-size: auto;
  }
  .accordion-button:not(.collapsed)::after {
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/circle-arrow-down.svg");
  }
}
@include media-breakpoint-up(lg) {
  .accordion-body a {
    color: $primary;
  }
}
.accordion-location-link a {
  @extend .text-black;
}#apply_form {.accordion-button::after {
    margin-left: 8px !important;
    width: 10px;
    height: 6px;
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/simple-arrow-down.svg");
    background-size: auto;
  }
  .accordion-button.accordion-button-show::after {
    transform: rotate(180deg);
  }
  .accordion-button:not(.collapsed) {
    background-color: white !important;
  }
}
.accordion-button.btn-plus::after {
  background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/plus.svg");
  width: 14px;
  height: 14px;
  background-size: auto;
}​
```
**_alumnus_card.scss**
```
.alumnus-card-width {
  width: 200px !important;
  @include media-breakpoint-up(md) {
    width: 264px !important;
  }
}
.alumnus-card-logo {
  bottom: -15px;
  right: 16px;
}
.alumnus-card-linkedin {
  padding: 0 0 3px 3px;
}
.global-alumnus-card {
  width: 200px;
}
.graduate-card-width {
  @include media-breakpoint-down(md) {
    width: 260px !important;
  }
}​
```
**_apply_card.scss**
```
.radio-card {
  font-size: $font-size-base;
  label {
    @extend .bg-info-5;
    transition: background-color .1s linear, color .1s linear;&:hover {
      @extend .bg-light-gray;
    }}
  input[type="radio"] {
    top: 26%;
    left: 3rem;&:checked ~ label {
      @extend .bg-secondary-tonic;
      @extend .text-white;
    }&:disabled ~ label {
      @extend .opacity-40;
    }}
}
.batch-card {
  padding: 0;
  font-size: $font-size-base;
  input[type="radio"] {
    position: fixed;
    opacity: 0;
    pointer-events: none;~ label {
      border: 2px solid transparent;
    }&:checked ~ label {
      border: 2px solid $secondary;
      border-radius: 4px;
    }&:focus ~ label {
      border: 2px solid $secondary;
      border-radius: 4px;
    }}
}​
```
**_apply_form.scss**
```
.apply-form {
  @extend .placeholder-info;
  @extend .select-dark;
  select:disabled {
    color: $info;
  }
  select:focus {
    box-shadow: 0 0 0 0.25rem $light-purple;
  }
}
.thanks-link::after {
  content: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right.svg");
  margin-left: 16px;
}#apply_form {.offcanvas-backdrop {
    @extend .z-1000;
  }
}​
```
**_button.scss**
```
.btn {
	@extend .fw-bold;
}
// NOTES(cedricmenteau): Add fixed arrow on mobile devices
@include media-breakpoint-down(md) {
	.btn-light,
	.btn-secondary-tonic,
	.btn-outline-dark {
		position: relative;
		padding-right: 49px !important;
		text-align: left;&:after {
			content: "";
			position: absolute;
			right: 26px;
			top: 50%;
			transform: translateY(-50%) scale(1.5);
			width: 11px;
			height: 9px;
		}
	}.btn-outline-dark:after {
		background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right.svg");
	}.btn-light:after {
		background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-dark-purple.svg");
	}}
.btn-light:hover {
	background-color: $cream !important;
	border-color: $cream !important;
}
.btn-light-gray {
	background-color: transparent !important;
	border: 1px solid black;
}
.btn-light-gray:hover {
	background-color: $light-gray !important;
}
.btn-cream-hover:hover {
  background-color: $cream !important;
}
.btn-primary.btn-white-arrow:hover {
	background-color: $primary !important;
}
.btn-light.btn-tonic-arrow:hover {
	background-color: $cream !important;
	border-color: $cream !important;
}
.btn-secondary-light {
  background-color: $cream !important;
  border-color: $cream !important;
  color: $secondary !important;
  padding: 0.6rem 1rem;
}
.btn-secondary-light:hover {
  background-color: $secondary !important;
  border-color: $secondary !important;
  color: white !important;
}
// NOTES(cedricmenteau): Add pseudo element for arrow on desktop devices
.btn-white-arrow:hover,
.btn-black-arrow:hover,
.btn-tonic-arrow:hover,
.btn-purple-arrow:hover,
.btn-sm.btn-white-arrow:hover,
.btn-sm.btn-black-arrow:hover,
.btn-sm.btn-tonic-arrow:hover,
.btn-sm.btn-purple-arrow:hover {
	position: relative;
	transition: 0.2s ease;&:after {
		content: "";
		position: absolute;
		top: 50%;
		transform: translateY(-50%) scale(1.5);
		width: 11px;
		height: 9px;
	}}
// NOTES(cedricmenteau): Create space for arrow on btn
.btn-white-arrow:hover,
.btn-black-arrow:hover,
.btn-tonic-arrow:hover,
.btn-purple-arrow:hover {
	padding-right: 49px !important;&:after {
		right: 26px;
	}}
// NOTES(cedricmenteau): Create space for arrow on btn-sm
.btn-sm.btn-white-arrow:hover,
.btn-sm.btn-black-arrow:hover,
.btn-sm.btn-tonic-arrow:hover,
.btn-sm.btn-purple-arrow:hover {
	padding-right: 40px !important;&:after {
		right: 17px;
	}}
.btn-white-arrow:hover {
	&:after {
		background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-white.svg");
	}
}
.btn-black-arrow:hover {
	&:after {
		background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right.svg");
	}
}
.btn-tonic-arrow:hover {
	&:after {
		background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-tonic.svg");
	}
}
.btn-purple-arrow:hover {
	&:after {
		background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-dark-purple.svg");
	}
}
// NOTES(cedricmenteau): Reset padding for submit input as input doesn't support :after pseudo element.
input[type="submit"].btn-light,
input[type="submit"].btn-secondary-tonic,
input[type="submit"].btn-outline-dark,
input[type="submit"].btn-sm {
	padding-right: 1.5rem !important;
}
// NOTES(annedj): Apply forms Buttons with static arrows and disabled state
.btn-static-arrow-light,
.btn-static-arrow-tonic {
  position: relative;
  &::after {
    content: "";
    position: absolute;
    top: 50%;
    transform: translateY(-50%) scale(1.5);
    width: 11px;
    height: 9px;
  }
}
.btn-static-arrow-light {
  padding-left: 40px !important;
  text-align: right;
  &::after {
    left: 17px;
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-left-tonic.svg");
  }
}
.btn-static-arrow-tonic {
  padding-right: 40px !important;
  text-align: left;
  &::after {
    right: 17px;
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-white.svg");
  }
  &:disabled {
    background-color: $light;
    border-color: $light;
    color: $secondary-tonic !important;
    @extend .opacity-40;
    &:after {
      background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-tonic.svg");
    }
  }
}
.btn-arrow {
  padding-right: 44px !important;
  text-align: left;
  position: relative;
  &::after {
    right: 22px;
    content: "";
    position: absolute;
    top: 50%;
    transform: translateY(-50%) scale(1.5);
    width: 11px;
    height: 9px;
  }
}
.btn-purple-to-white-arrow {
  &::after {
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-tonic.svg");
  }
  &:hover {
    &::after {
      background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-white.svg");
    }
  }
}
.btn-white-to-purple-arrow {
  &::after {
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-white.svg");
  }
  &:hover {
    &::after {
      background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-tonic.svg");
    }
  }
}
.btn-static-arrow-white {
  &::after {
    background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-white.svg");
  }
}
.btn-close-white {
  opacity: 1 !important;
  svg {
    fill: $white !important;
  }
}​
```
*calendar_iframe.scss*
```
.meetings-iframe-container, .calendly-inline-widget {
  min-width: 300px;
  min-height: 516px;
}
.meetings-iframe-container {
  height: 565px;
}
.embed-calendar-xl {
  height: 640px;
}
.calendly-inline-widget {
  height: 500px;
  @include media-breakpoint-up(md) {
    height: 550px;
  }
}
.calendar-locked {
  position: relative;
  filter: blur(1px);
  opacity: 0.4;
  // Block calendly user interactions
  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
}
.routing-calendar {
  height: 770px;
  @include media-breakpoint-up(md) {
    height: 660px;
  }
}​
```
**_campus_card.scss**
```
.campus-card-thumbnail {
	max-height: 163px;@include media-breakpoint-up(sm) {
    max-height: auto;}
}
.campus-filter-cta {
  &::after {
    content: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-down-purple.svg");
    margin-left: 8px;
    @include media-breakpoint-down(md) {
      position: relative;
      margin-top: 4px;
    }
    @include media-breakpoint-down(md) {
      position: absolute;
      transform: scale(0.9);
      top: 6px;
      width: 0;
    }
  }
  &:hover {
    &::after {
      content: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-down-white.svg");
    }
  }
}
.campus-filter-link {
  background-color: rgba(0,0,0,0.05);
  color: rgba(0,0,0,0.8);
  @include media-breakpoint-down(md) {
    position: relative;
    margin-top: 4px;
  }
  &:hover, &:focus {
    background-color: $secondary-light;
    color: $secondary;
  }
  &::after {
    content: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/close.svg");
    margin-left: 8px;
    @include media-breakpoint-down(md) {
      position: absolute;
      transform: scale(0.8);
      top: 12px;
      width: 0;
    }
  }
}​
```
**_campus_pictures.scss**
```
.campus-card-width {
  width: 316px !important;
}
.campus-picture {
  height: 400px;
}​
```
**_card.scss**
```
.card.shadow-elevation-2:hover {
	transition: 0.2s ease;
	@extend .shadow-elevation-4;
}
.card.shadow-elevation-4:hover {
	transition: 0.2s ease;
	@extend .shadow-elevation-8;
}
.card:hover .btn-tonic-arrow {
	position: relative;
	transition: 0.2s ease;
	padding-right: 40px !important;
	background-color: $tonic-purple !important;
	color: white !important;&:after {
		content: "";
		position: absolute;
		top: 50%;
		right: 17px;
		transform: translateY(-50%) scale(1.5);
		width: 11px;
		height: 9px;
		background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-white.svg");
	}}
.card-hover-invert-btn:hover {
  .btn-outline-primary {
    @extend .text-white;
    @extend .bg-primary;
    &::after {
      background-image: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-white.svg");
    }
  }
}​
```
**_carousel.scss**
```
.carousel-custom {
  .carousel-control-prev,
  .carousel-control-next {
    position: absolute;
    top: -60px;
    width: 32px;
    height: 32px;
    background-color: transparent;
    border: 1px solid #670BFF4D;
    border-radius: 4px;
    color: $primary;
    opacity: 1;
    transition: .5s background-color ease;
  }
  .carousel-control-prev {
    left: auto;
    right: 52px;
  }
  .carousel-control-next {
    left: auto;
    right: 13px;
  }
  .carousel-control-prev-icon {
    margin-left: -2px;
    width: 10px;
  }
  .carousel-control-next-icon  {
    width: 10px;
    margin-left: 4px;
  }
}
.carousel-recruitment {
  .carousel-control-prev,
  .carousel-control-next {
    position: absolute;
    top: 50%;
    width: 40px;
    height: 40px;
    background-color: $light-purple;
    border-radius: 50%;
    transform: translateY(-50%);
  }
  .carousel-control-prev-icon {
    margin-left: -2px;
    width: 13px;
  }
  .carousel-control-next-icon  {
    width: 13px;
    margin-left: 4px;
  }
}​
```
/**_header.scss**
```
.hero-header {
  height: 575px;
  @include media-breakpoint-up(md) {
    height: 755px;
  }
  @include media-breakpoint-up(xl) {
    height: 670px;
  }
  .hero-main-title {
    font-weight: 500;
    line-height: 110%;
  }
  .hero-picture {
    width: 100% !important;
    max-width: calc(100% - 24px);
    height: 100% !important;
  }
  .hero-picture-overlay:after {
    content: "";
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
    background: radial-gradient(circle, rgba(255,255,255,0) 0%, rgba(0,0,0,0.15) 100%);
  }
  .hero-caption {
    strong {
      font-size: 16px;
    }
  }
}
.desaturated {
  filter: brightness(0) invert(1);
}
.hero-with-block-header {
  position: relative;
  width: 100%;
  overflow: hidden;
  padding: 0 16px;
  box-sizing: border-box;
  .hero-picture {
    width: 100% !important;
    max-withd: 100% !important;
    height: 100% !important;
    z-index: 0;img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center center;
      display: block;
    }}
}​
```
**_hubspot_form.scss**
```
.hs-form-iframe {
  width: 100% !important;
}
.hs-input {
  @extend .form-control;
}
.hs-input::placeholder {
  color: var(--bs-gray-500);
  opacity: 1; // Firefox
}
.hs-form-field {
  @extend .row;
  @extend .mb-3;
}
.hs-form-field label {
  margin-bottom: 0.5rem;
  @extend .fw-bold;
  @extend .col-xl-3;
  @extend .fs-15;
  @extend .d-flex;
  @extend .align-items-center;
  @include media-breakpoint-up(md) {
    margin-bottom: 0;
  }
}
.hs-form-field .input {
  @extend .col-xl-9;
}
.hs-fieldtype-select select {
  @extend .form-select;
  @extend .text-black;
}
.hs_message label {
  align-items: flex-start !important;
  @include media-breakpoint-up(md) {
    margin-top: 6px;
  }
}
.hs-button {
  @extend .btn;
  @extend .w-100;
  @extend .mt-3;
}
.hs-button.primary {
  @extend .btn-primary;
  @extend .position-relative;
  @extend .text-center;
  padding: 0.75rem 1.5rem;
  min-width: auto;
}
.hs-richtext {
  @extend .text-info;
  @extend .fs-12;
}
.hs-form-booleancheckbox-display {
  @extend .fs-12;
  @extend .form-check;
  @extend .position-relative;
}
.hs-form-booleancheckbox-display .hs-input {
  @extend .form-check-input;
  @extend .p-0;
  @extend .position-absolute;
  margin: 0 0 0 -1rem;
  width: 15px;
  top: 3px;
}
.legal-consent-container {
  .hs-form-field {
    @extend .row;
    @extend .mb-0;
  }
  .hs-form-field label {
    margin-bottom: 0.5rem;
    color: var(--bs-gray-500);
    @extend .fw-normal;
    @extend .col-md-12;
  }
  .hs-form-field .input {
    @extend .col-md-12;
  }
}
.hs-form-booleancheckbox-display span {
  @extend .form-check-label;
  @extend .ms-2;
  @extend .fs-12;
}
.hs-dependent-field .inputs-list {
  @extend .list-unstyled;
  @extend .ps-0;
}
.hs-error-msgs {
  @extend .list-unstyled;
  @extend .col-xl-9;
  @extend .offset-xl-3;
  @extend .ps-xl-3;
  @extend .mb-0;
}
.hs-error-msgs li {
  @extend .invalid-feedback;
  display: block !important;
}
.hs-input.invalid.error {
  @extend .is-invalid;
}
.hs-error-msgs li .hs-error-msg {
  @extend .invalid-feedback;
  display: block !important;
}
.hs_error_rollup .hs-error-msgs li {
  font-size: inherit !important;
}
.hs-field-desc {
  @extend .fs-12;
}
.hs-form-required {
  @extend .d-none;
}#skill-course-advisor-form {.hs-fieldtype-textarea .input {
    @extend .w-100;
  }
}
.form-columns-1 label,
.form-columns-1 .input,
.form-columns-1 .input input,
.form-columns-1 .input select {
  width: 100% !important;
  margin: 0 !important;
}
.form-columns-1 .input .hs-form-booleancheckbox-display .hs-input {
  margin: 0 0 0 -1rem !important;
  width: 15px !important;
}
.form-columns-1 .hs-error-msgs {
  margin-left: 0 !important;
}
.form-columns-2 {
  display: flex;
  justify-content: space-between;
}
.form-columns-2 label,
.form-columns-2 .input {
  width: 100% !important;
}
.hs-fieldtype-phonenumber {
  text-align: left;
}
// NEW FORM BUILDER
.hsfc-FieldLabel {
  @extend .fw-bold;
}
.hsfc-TextInput {
  @extend .form-control;
  border: none !important;
}
.hsfc-DropdownOptions, .hsfc-PhoneInput__FlagAndCaret {
  border: none !important;
}
.hsfc-Button {
  background-color: $primary !important;
  @extend .btn-primary;
  @extend .position-relative;
  @extend .text-center;
  padding: 0.75rem 1.5rem;
  min-width: auto;
  width: 100% !important;
  border-radius: .5rem !important;
}
.hsfc-Step__Content {
  padding: 0 !important;
}​
```
**_program_card.scss**
```
.program-card-width {
	@extend .w-100;@include media-breakpoint-up(md) {
		width: 312px !important;
	}.card:hover {
		@extend .shadow-elevation-8; 
	}}
.program-card-width-sm {
  @extend .w-100;
  @include media-breakpoint-up(md) {
    width: 260px !important;
  }
  .card:hover {
    @extend .shadow-elevation-8;
  }
}
.program-card-thumbnail {
	height: 76px;
	width: 76px;@include media-breakpoint-up(md) {
		height: 204px;
		width: 100%;
	}}
.program-card-thumbnail-sm {
  height: 76px;
  width: 76px;
  @include media-breakpoint-up(md) {
    height: 150px;
    width: 100%;
  }
}
.skill-course-card-link {
  display: flex;
  &::after {
    content: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-purple.svg");
    margin-left: 6px;
    transition: all 1s ease;
  }
  &:hover {
    color: $primary !important;
    font-weight: bold;
    font-variation-settings: 'wght' 650 !important;
    &::after {
      content: url("https://4419217.fs1.hubspotusercontent-na1.net/hubfs/4419217/icons/icons-v5/arrow-right-purple.svg");
      transform: translateX(50%);
    }
  }
}​
```
**_vertical_carousel.scss**
```
.custom-vertical-carousel {
  .active {
    @extend .bg-transparent;
    @extend .text-secondary-tonic;
    @extend .border-secondary-tonic;
    @extend .fw-bold;
  }
}​
```
**_background.scss**
```
.bg-cream-mobile-only {
	@extend .bg-cream;@include media-breakpoint-up(md) {
		background-color: transparent !important;
	}}
.bg-white-mobile-only {
	@extend .bg-white;@include media-breakpoint-up(md) {
		background-color: $cream !important;
	}}
.bg-cream-to-secondary-dark {
	@extend .bg-cream;@include media-breakpoint-up(md) {
		background-color: $secondary-dark !important;
	}}
.bg-white-to-transparent {
  @extend .bg-body;@include media-breakpoint-up(md) {
		background-color: transparent !important;
	}}
.bg-oversized {
	@extend .position-relative;@include media-breakpoint-up(md) {
		&:after {
			content: "";
			position: absolute;
			top: -0.5rem;
			left: -2rem;
			width: calc(100% + 4rem);
			height: calc(100% + 1rem);
			background-color: $cream;
			border-radius: 1rem;
			z-index: -1;
		}
	}}​
```
## Related
- [[Content]]
- [[Events]]
