import * as React from "react";
import classNames from "classnames";
import {Icon} from "@blueprintjs/core";
import {AppStore} from "stores";
import "./CustomIcons.scss";

export declare type CustomIconName =
    | "contour"
    | "center"
    | "regionList"
    | "spatialProfiler"
    | "spectralProfiler"
    | "stokes"
    | "spectralLineQuery"
    | "smoothing"
    | "moments"
    | "distanceMeasuring"
    | "cursor"
    | "line"
    | "polyline"
    | "imageFitting"
    | "lineFitting"
    | "vectorOverlay";

export class CustomIcon extends React.Component<{icon: CustomIconName; size?: number}> {
    static readonly SIZE_STANDARD = 16;
    static readonly SIZE_LARGE = 20;

    public render() {
        const className = classNames("custom-icon", "bp3-icon", {"dark-theme": AppStore.Instance.darkTheme});
        const size = (this.props.size ? this.props.size : CustomIcon.SIZE_STANDARD) + "px";
        const content = (
            <span className={className}>
                <svg width={size} height={size} viewBox="0 0 16 16">
                    {icons[this.props.icon]}
                </svg>
            </span>
        );
        return <Icon icon={content} />;
    }
}

// copy content of tag <path/> in svg, and turn attributes fill-rule/clip-rule into fillRule/clipRule.
const contourSvg = (
    <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="M 13.3086,13.326331 A 7.489923,8.4952736 45 0 1 2.0053593,14.037221 7.489923,8.4952736 45 0 1 2.7162497,2.7339802 7.489923,8.4952736 45 0 1 14.01949,2.02309 7.489923,8.4952736 45 0 1 13.3086,13.326331 Z
        M 13.148613,12.347604 A 6.6468272,7.6124401 40 0 1 3.1636657,13.906573 6.6468272,7.6124401 40 0 1 2.9650831,3.8026076 6.6468272,7.6124401 40 0 1 12.95003,2.2436383 6.6468272,7.6124401 40 0 1 13.148613,12.347604 Z
        M 10.882979,12.264102 A 4.8685541,5.7219758 50 0 1 3.3702451,12.212588 4.8685541,5.7219758 50 0 1 4.6240863,4.8050444 4.8685541,5.7219758 50 0 1 12.136821,4.8565581 4.8685541,5.7219758 50 0 1 10.882979,12.264102 Z
        M 10.33713,11.668778 A 4.0524521,4.8181229 50 0 1 4.0413674,11.66145 4.0524521,4.8181229 50 0 1 5.1273981,5.4600614 4.0524521,4.8181229 50 0 1 11.42316,5.4673901 4.0524521,4.8181229 50 0 1 10.33713,11.668778 Z
        M 7.9142814,10.852556 A 2.047241,2.547725 60 0 1 4.6842662,10.353456 2.047241,2.547725 60 0 1 5.8670405,7.3066306 2.047241,2.547725 60 0 1 9.0970556,7.8057308 2.047241,2.547725 60 0 1 7.9142814,10.852556 Z
        M 7.5029842,10.217581 A 1.2341059,1.684913 60 0 1 5.426754,9.9912708 1.2341059,1.684913 60 0 1 6.2688783,8.0800472 1.2341059,1.684913 60 0 1 8.3451088,8.3063578 1.2341059,1.684913 60 0 1 7.5029842,10.217581 Z"
    />
);

const centerSvg = (
    <g fillRule="evenodd" clipRule="evenodd">
        <circle className="st0" cx="8" cy="8" r="2" />
        <path
            className="st0"
            d="M2.6,4H2C1.4,4,1,4.4,1,5s0.4,1,1,1h3c0.1,0,0.3,0,0.4-0.1c0.2-0.1,0.4-0.3,0.5-0.5C6,5.2,6,5.1,6,5V2
		    c0-0.6-0.4-1-1-1S4,1.4,4,2v0.6L1.7,0.3c-0.4-0.4-1-0.4-1.4,0s-0.4,1,0,1.4L2.6,4z"
        />
        <path
            className="st0"
            d="M10.1,5.4c0.1,0.2,0.3,0.4,0.5,0.5S10.9,6,11.1,6h3c0.6,0,1-0.4,1-1s-0.4-1-1-1h-0.6l2.3-2.3
		    c0.4-0.4,0.4-1,0-1.4c-0.4-0.4-1-0.4-1.4,0L12,2.6V2c0-0.6-0.4-1-1-1s-1,0.4-1,1v3C10,5.1,10,5.2,10.1,5.4z"
        />
        <path
            className="st0"
            d="M13.4,12H14c0.6,0,1-0.4,1-1s-0.4-1-1-1h-3c-0.1,0-0.3,0-0.4,0.1c-0.2,0.1-0.4,0.3-0.5,0.5
		    C10,10.8,10,10.9,10,11v3c0,0.6,0.4,1,1,1s1-0.4,1-1v-0.6l2.3,2.3c0.4,0.4,1,0.4,1.4,0c0.4-0.4,0.4-1,0-1.4L13.4,12z"
        />
        <path
            className="st0"
            d="M5.9,10.6c-0.1-0.2-0.3-0.4-0.5-0.5C5.2,10,5.1,10,4.9,10H2c-0.6,0-1,0.4-1,1s0.4,1,1,1h0.6l-2.3,2.3
		    c-0.4,0.4-0.4,1,0,1.4c0.4,0.4,1,0.4,1.4,0L4,13.4V14c0,0.6,0.4,1,1,1s1-0.4,1-1v-3C6,10.9,6,10.8,5.9,10.6z"
        />
    </g>
);

const regionListSvg = (
    <g>
        <g id="Layer_1-2" data-name="Layer 1">
            <path className="cls-1" d="M1,6H8A.9448.9448,0,0,0,9,5,.9448.9448,0,0,0,8,4H1A1,1,0,0,0,1,6Zm9,6H1a1,1,0,0,0,0,2h9a1,1,0,0,0,0-2Zm0-4H1a1,1,0,0,0,0,2h9a.9448.9448,0,0,0,1-1A.9448.9448,0,0,0,10,8Z" />
        </g>
        <path d="M15.6169,5.6628a2.6806,2.6806,0,0,1-.0932-.4019,3.6675,3.6675,0,0,1-.04-.4307q-.0089-.2191-.0244-.43a3.8144,3.8144,0,0,0-.0694-.4062,1.2166,1.2166,0,0,0-.1382-.3533A.8941.8941,0,0,0,15,3.3679a1.0366,1.0366,0,0,0-.4106-.1623V3.1894a1.2325,1.2325,0,0,0,.7676-.5444,1.7581,1.7581,0,0,0,.24-.9262A1.3974,1.3974,0,0,0,15.13.6063,1.9077,1.9077,0,0,0,13.8339.2h-2.73V6h.7722V3.5223h1.8847a1.0267,1.0267,0,0,1,.4549.0852.7677.7677,0,0,1,.2763.2275.9485.9485,0,0,1,.154.3332q.0486.1908.0813.4022a2.9046,2.9046,0,0,1,.049.43q.0078.22.0158.41a2.4616,2.4616,0,0,0,.037.3455A.48.48,0,0,0,14.9386,6H15.8A.9979.9979,0,0,1,15.6169,5.6628ZM14.423,2.6735a1.1087,1.1087,0,0,1-.4264.1583,3.079,3.079,0,0,1-.5117.0406H11.8765V.85h1.9171a1.0026,1.0026,0,0,1,.788.276,1.0431,1.0431,0,0,1,.2433.7149,1.0608,1.0608,0,0,1-.11.516A.8646.8646,0,0,1,14.423,2.6735Z" />
    </g>
);

const spatialProfilerSvg = (
    <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="m12.773438,9.978644l-1.243281,0l-1.447656,-2.171484l-0.017031,0.008516c-0.153281,-0.229922 -0.400234,-0.391719 -0.698281,-0.391719c-0.366172,0 -0.672734,0.229922 -0.791953,0.553516l-0.008516,0l-1.439141,3.840547l-1.175156,-7.085l-0.017031,0
        c-0.068125,-0.400234 -0.400234,-0.715313 -0.826016,-0.715313c-0.349141,0 -0.655703,0.212891 -0.783437,0.519453l0,0l0,0c0,0 0,0 0,0l-2.333281,5.441484l-1.141094,0c-0.468359,0 -0.851562,0.383203 -0.851562,0.851563
        c0,0.468359 0.383203,0.851563 0.851562,0.851563l1.703125,0c0.349141,0 0.655703,-0.212891 0.783438,-0.519453l0,0l0,0c0,0 0,0 0,0l1.405078,-3.287031l1.22625,7.348984l0.017031,0c0.068125,0.400234 0.400234,0.715312 0.826016,0.715312
        c0.366172,0 0.672734,-0.229922 0.791953,-0.553516l0.008516,0l1.967109,-5.254141l0.783437,1.175156l0.017031,-0.008516c0.144766,0.221406 0.391719,0.383203 0.689766,0.383203l1.703125,0c0.468359,0 0.851563,-0.383203 0.851563,-0.851563
        c0,-0.468359 -0.383203,-0.851563 -0.851563,-0.851563z

        M 8.3904279,2.3870306 6.5797618,4.9256964 h 0.961333 L 8.8850944,2.9283637 10.229094,4.9256964 h 1.017333 L 9.3797609,2.3216973 11.041094,0.10036468 h -0.952 L 8.8850944,1.7896974 7.7277615,0.10036468 h -1.017333 z
        M 13.818489,5.5696962 q -0.14,0.3546665 -0.28,0.5973331 -0.130667,0.2426666 -0.298667,0.3919999 -0.158666,0.1586666 -0.364,0.2239999 -0.196,0.074667 -0.457333,0.074667 -0.14,0 -0.28,-0.018667 -0.14,-0.018667 -0.270666,
        -0.065333 V 6.045696 q 0.102666,0.046667 0.233333,0.074667 0.14,0.037333 0.233333,0.037333 0.242667,0 0.401333,-0.1213333 0.168,-0.112 0.252,-0.3266666 L 13.314489,4.8976964 11.401156,0.10036468 h 0.896 l 1.409333,
        3.94799862 h 0.01867 l 1.353333,-3.94799862 h 0.84 z"
    />
);

const spectralProfilerSvg = (
    <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="m12.773438,9.978644l-1.243281,0l-1.447656,-2.171484l-0.017031,0.008516c-0.153281,-0.229922 -0.400234,-0.391719 -0.698281,-0.391719c-0.366172,0 -0.672734,0.229922 -0.791953,0.553516l-0.008516,0l-1.439141,3.840547l-1.175156,-7.085l-0.017031,0
        c-0.068125,-0.400234 -0.400234,-0.715313 -0.826016,-0.715313c-0.349141,0 -0.655703,0.212891 -0.783437,0.519453l0,0l0,0c0,0 0,0 0,0l-2.333281,5.441484l-1.141094,0c-0.468359,0 -0.851562,0.383203 -0.851562,0.851563
        c0,0.468359 0.383203,0.851563 0.851562,0.851563l1.703125,0c0.349141,0 0.655703,-0.212891 0.783438,-0.519453l0,0l0,0c0,0 0,0 0,0l1.405078,-3.287031l1.22625,7.348984l0.017031,0c0.068125,0.400234 0.400234,0.715312 0.826016,0.715312
        c0.366172,0 0.672734,-0.229922 0.791953,-0.553516l0.008516,0l1.967109,-5.254141l0.783437,1.175156l0.017031,-0.008516c0.144766,0.221406 0.391719,0.383203 0.689766,0.383203l1.703125,0c0.468359,0 0.851563,-0.383203 0.851563,-0.851563
        c0,-0.468359 -0.383203,-0.851563 -0.851563,-0.851563z

        M 11.225128,5.0020008 v 0.6933355 h 4.650681 V 4.8953338 H 12.355798 L 15.726475,0.79932088 V 0.18065225 h -4.288013 v 0.80000253 h 3.114676 z"
    />
);

const stokesSvg = (
    <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="m12.773438,9.978644l-1.243281,0l-1.447656,-2.171484l-0.017031,0.008516c-0.153281,-0.229922 -0.400234,-0.391719 -0.698281,-0.391719c-0.366172,0 -0.672734,0.229922 -0.791953,0.553516l-0.008516,0l-1.439141,3.840547l-1.175156,-7.085l-0.017031,0
        c-0.068125,-0.400234 -0.400234,-0.715313 -0.826016,-0.715313c-0.349141,0 -0.655703,0.212891 -0.783437,0.519453l0,0l0,0c0,0 0,0 0,0l-2.333281,5.441484l-1.141094,0c-0.468359,0 -0.851562,0.383203 -0.851562,0.851563
        c0,0.468359 0.383203,0.851563 0.851562,0.851563l1.703125,0c0.349141,0 0.655703,-0.212891 0.783438,-0.519453l0,0l0,0c0,0 0,0 0,0l1.405078,-3.287031l1.22625,7.348984l0.017031,0c0.068125,0.400234 0.400234,0.715312 0.826016,0.715312
        c0.366172,0 0.672734,-0.229922 0.791953,-0.553516l0.008516,0l1.967109,-5.254141l0.783437,1.175156l0.017031,-0.008516c0.144766,0.221406 0.391719,0.383203 0.689766,0.383203l1.703125,0c0.468359,0 0.851563,-0.383203 0.851563,-0.851563
        c0,-0.468359 -0.383203,-0.851563 -0.851563,-0.851563z

        M 12.043082,4.1413775 h -0.906669 q 0.02133,0.5120017 0.213334,0.8746695 0.192,0.3520011 0.512001,0.5760018 0.320001,0.213334 0.736003,0.3093343 0.416001,0.096 0.874669,0.096 0.416002,0 0.832003,-0.085334 0.426668,-0.074667 0.757336,
        -0.2773342 0.341334,-0.2026673 0.544001,-0.533335 0.213334,-0.3306677 0.213334,-0.8320026 0,-0.394668 -0.16,-0.6613355 Q 15.50976,3.341375 15.253759,3.1707078 15.008425,2.9893739 14.677757,2.8827069 14.357756,2.7760399 14.016422,
        2.701373 13.696421,2.6267061 13.37642,2.5627059 13.056419,2.488039 12.800418,2.3920387 12.544417,2.2853717 12.37375,2.1360379 q -0.16,-0.1600005 -0.16,-0.3946679 0,-0.213334 0.106667,-0.3413344 0.106667,-0.1386672 0.277334,-0.2133341 0.170667,
        -0.085334 0.373334,-0.1173337 0.213334,-0.032 0.416002,-0.032 0.224,0 0.437334,0.053334 0.224001,0.042667 0.405335,0.1493338 0.181334,0.1066671 0.298668,0.288001 0.117333,0.1706672 0.138667,0.4373347 H 15.57376 Q 15.54176,1.4640358 15.360426,
        1.133368 15.179092,0.79203363 14.869758,0.60003303 14.57109,0.39736572 14.176422,0.32269882 13.781755,0.23736521 13.31242,0.23736521 q -0.362668,0 -0.736003,0.0960003 -0.362667,0.0853336 -0.661335,0.27733421 -0.288001,0.1813339 -0.480002,
        0.48000147 -0.181333,0.2986677 -0.181333,0.714669 0,0.533335 0.266667,0.8320026 0.266668,0.2986676 0.661335,0.4693348 0.405335,0.1600005 0.87467,0.2560008 0.469335,0.085334 0.864003,0.2026673 0.405334,0.106667 0.672002,0.2880009 0.266667,
        0.1813339 0.266667,0.5333351 0,0.2560008 -0.128,0.426668 -0.128001,0.1600005 -0.330668,0.2453341 -0.192,0.085334 -0.426668,0.1173337 -0.234667,0.032 -0.448001,0.032 -0.277334,0 -0.544002,-0.053334 -0.256001,-0.053333 -0.469335,
        -0.1706672 -0.202667,-0.1280004 -0.330668,-0.3306677 -0.128,-0.213334 -0.138667,-0.5120017 z"
    />
);

const spectralLineQuerySvg = (
    <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="m12.773438,9.978644l-1.243281,0l-1.447656,-2.171484l-0.017031,0.008516c-0.153281,-0.229922 -0.400234,-0.391719 -0.698281,-0.391719c-0.366172,0 -0.672734,0.229922 -0.791953,0.553516l-0.008516,0l-1.439141,3.840547l-1.175156,-7.085l-0.017031,0c-0.068125,-0.400234 -0.400234,-0.715313 -0.826016,-0.715313c-0.349141,0 -0.655703,0.212891 -0.783437,0.519453l0,0l0,0c0,0 0,0 0,0l-2.333281,5.441484l-1.141094,0c-0.468359,0 -0.851562,0.383203 -0.851562,0.851563c0,0.468359 0.383203,0.851563 0.851562,0.851563l1.703125,0c0.349141,0 0.655703,-0.212891 0.783438,-0.519453l0,0l0,0c0,0 0,0 0,0l1.405078,-3.287031l1.22625,7.348984l0.017031,0c0.068125,0.400234 0.400234,0.715312 0.826016,0.715312c0.366172,0 0.672734,-0.229922 0.791953,-0.553516l0.008516,0l1.967109,-5.254141l0.783437,1.175156l0.017031,-0.008516c0.144766,0.221406 0.391719,0.383203 0.689766,0.383203l1.703125,0c0.468359,0 0.851563,-0.383203 0.851563,-0.851563c0,-0.468359 -0.383203,-0.851563 -0.851563,-0.851563z
        M15.766554,6.815244l-1.355908,-1.360986c0.355481,-0.553535 0.563692,-1.208637 0.563692,-1.909443c0,-1.965304 -1.58951,-3.554814 -3.554814,-3.554814s-3.554814,1.58951 -3.554814,3.554814s1.58951,3.554814 3.554814,3.554814c0.705885,0 1.360986,-0.213289 1.909443,-0.563692l1.360986,1.355908c0.137114,0.137114 0.33009,0.223445 0.5383,0.223445c0.421499,0 0.761746,-0.340247 0.761746,-0.761746c0,-0.208211 -0.086331,-0.401186 -0.223445,-0.5383zm-4.34703,-0.731276c-1.401613,0 -2.539153,-1.137541 -2.539153,-2.539153s1.137541,-2.539153 2.539153,-2.539153s2.539153,1.137541 2.539153,2.539153s-1.137541,2.539153 -2.539153,2.539153z"
    />
);

const profileSmoothingSvg = <path strokeWidth="2.42095" strokeLinecap="round" fill="none" d="M 1.413244,14.6062 H 3.9277429 V 8.378223 H 6.9751347 V 1.4946692 H 9.5085614 L 14.575415,14.576401" />;

const momentGeneratorSvg = (
    <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="M 0.81609227,1.2562455 V 14.58427 H 3.5600972 V 5.2322526 h 0.037333 L 6.8641032,14.58427 H 9.1227739 L 12.389446,5.1389191 h 0.03733 V 14.58427 h 2.744005 V 1.2562455 H 11.045444 L 8.0961054,10.421595 H 8.058772 L 4.941433,1.2562455 Z"
    />
);

const distanceMeasuringSvg = (
    <path
        transform="scale(1.6, 1.6) translate(-2.5, -3)"
        d="M 11.390625 11.390625 L 10.824219 11.960938 L 10.542969 11.679688 L 11.113281 11.113281 L 9.769531 9.769531 L 9.199219 10.335938 L 8.921875 10.054688 L 9.488281 9.488281 L 8.144531 8.144531 L 7.574219 8.710938 L 7.296875 8.433594 L 7.863281 7.863281 L 6.511719 6.511719 L 5.953125 7.078125 L 5.664062 6.800781 L 6.230469 6.230469 L 4.886719 4.886719 L 4.320312 5.457031 L 4.039062 5.167969 L 4.609375 4.601562 L 3.199219 3.199219 L 3.199219 11.601562 C 3.199219 12.265625 3.734375 12.800781 4.398438 12.800781 L 12.800781 12.800781 Z M 4.800781 11.199219 L 4.800781 7.0625 L 8.9375 11.199219 Z M 4.800781 11.199219 "
    />
);

const cursorSvg = (
    <path
        transform="scale(0.9) translate(-1, -1)"
        d="M17.09,18.5l-3.47-3.47L12.5,18L10,10l8,2.5l-2.97,1.11l3.47,3.47L17.09,18.5z M10,3.5c-3.58,0-6.5,2.92-6.5,6.5 s2.92,6.5,6.5,6.5c0.15,0,0.3-0.01,0.45-0.02l0.46,1.46C10.61,17.98,10.31,18,10,18c-4.42,0-8-3.58-8-8s3.58-8,8-8l0,0 c4.42,0,8,3.58,8,8c0,0.31-0.02,0.61-0.05,0.91l-1.46-0.46c0.01-0.15,0.02-0.3,0.02-0.45C16.5,6.42,13.58,3.5,10,3.5 M10,6.5 c-1.93,0-3.5,1.57-3.5,3.5c0,1.76,1.31,3.23,3.01,3.47L10,15c0,0-0.01,0-0.01,0C7.23,15,5,12.76,5,10c0-2.76,2.24-5,5-5l0,0 c2.76,0,5,2.23,5,4.99c0,0,0,0.01,0,0.01l-1.53-0.49C13.23,7.81,11.76,6.5,10,6.5"
    />
);

const lineSvg = (
    <path
        transform="translate(2.5, -3.5) rotate(45, 8, 8) scale(1.0, 1.6) rotate(-15, 8, 8)"
        fillRule="evenodd"
        clipRule="evenodd"
        d="M10,2C9.54,2,9.15,2.31,9.04,2.73l-2.99,9.96C6.02,12.79,6,12.89,6,13 c0,0.55,0.45,1,1,1c0.46,0,0.85-0.31,0.96-0.73l2.99-9.96C10.98,3.21,11,3.11,11,3C11,2.45,10.55,2,10,2z"
    />
);

const polylineSvg = (
    <path
        transform="scale(0.75) translate(-1.5, -1) rotate(-5, 9, 9)"
        d="M23,8c0,1.1-0.9,2-2,2c-0.18,0-0.35-0.02-0.51-0.07l-3.56,3.55C16.98,13.64,17,13.82,17,14c0,1.1-0.9,2-2,2s-2-0.9-2-2 c0-0.18,0.02-0.36,0.07-0.52l-2.55-2.55C10.36,10.98,10.18,11,10,11s-0.36-0.02-0.52-0.07l-4.55,4.56C4.98,15.65,5,15.82,5,16 c0,1.1-0.9,2-2,2s-2-0.9-2-2s0.9-2,2-2c0.18,0,0.35,0.02,0.51,0.07l4.56-4.55C8.02,9.36,8,9.18,8,9c0-1.1,0.9-2,2-2s2,0.9,2,2 c0,0.18-0.02,0.36-0.07,0.52l2.55,2.55C14.64,12.02,14.82,12,15,12s0.36,0.02,0.52,0.07l3.55-3.56C19.02,8.35,19,8.18,19,8 c0-1.1,0.9-2,2-2S23,6.9,23,8z"
    />
);

const pvSvg = (
    <>
        <path
            fillRule="evenodd"
            clipRule="evenodd"
            d="M 0.10806581 2.6739215 H 4.3993143 q 1.2724428 0 2.0514895,0.794923 0.7790466 0.787763 0.7790466 2.220058 0,1.231773 -0.6946498 2.148442 -0.69465 0.909507 -2.1358863,0.909507 H 1.3999848 V 13.194128 H 0.10806581 Z m 5.81688139,3.022142 q 0 -1.160159 -0.7790465 -1.575524 Q 4.717425 3.8985335 3.9708386 3.8985335 H 1.3999848 v 3.645191 h 2.5708538 q 0.8699355 0 1.408776 -0.408204 0.5453326 -0.408205 0.5453326 -1.439457 Z"
        />
        <path fillRule="evenodd" clipRule="evenodd" d="m 8.6774259,2.6739215 2.8316891,8.9590055 2.798138,-8.9590055 h 1.496366 L 12.206973,13.194128 H 10.791128 L 7.2011905,2.6739215 Z" />
    </>
);

// Adapted creative commons license icon https://www.svgrepo.com/svg/66474/rainfall
const vectorOverlaySvg = (
    <g transform="translate(0, -12) scale(0.03, 0.03)">
        <g className="st0">
            <path
                d="M10.025,622.148c2.6,0,5.1-0.9,7-2.9l61.8-61.8c3.9-3.9,3.9-10.2,0-14.1c-3.9-3.9-10.2-3.9-14.1,0l-61.8,61.8
				c-3.9,3.9-3.9,10.2,0,14.1C4.925,621.148,7.425,622.148,10.025,622.148z"
            />
            <path
                d="M145.725,622.148c2.6,0,5.1-0.9,7-2.9l61.8-61.8c3.9-3.9,3.9-10.2,0-14.1c-3.9-3.9-10.2-3.9-14.1,0l-61.8,61.8
				c-3.9,3.9-3.9,10.2,0,14.1C140.625,621.148,143.125,622.148,145.725,622.148z"
            />
            <path
                d="M281.425,622.148c2.6,0,5.2-0.9,7.1-3l60.9-61.8c3.9-3.9,3.8-10.2-0.1-14.1c-3.9-3.9-10.2-3.8-14.1,0.1l-60.9,61.8
				c-3.9,3.9-3.8,10.2,0.1,14.1C276.325,621.148,278.925,622.148,281.425,622.148z"
            />
            <path
                d="M416.225,622.148c2.5,0,5.1-0.9,7-2.9l61.8-61.8c3.9-3.9,3.9-10.2,0-14.1c-3.9-3.9-10.2-3.9-14.1,0l-61.8,61.8
				c-3.9,3.9-3.9,10.2,0,14.1C411.125,621.148,413.625,622.148,416.225,622.148z"
            />
            <path
                d="M64.725,754.948c2,1.9,4.5,2.9,7.1,2.9c2.6,0,5.2-0.9,7-2.9l61.8-61.8c3.9-3.9,3.9-10.2,0-14.1c-3.9-3.9-10.2-3.9-14.1,0
				l-61.8,61.8C60.825,744.748,60.825,751.048,64.725,754.948z"
            />
            <path
                d="M200.525,754.948c1.9,1.9,4.5,2.9,7,2.9h0c2.6,0,5.2-1,7.1-3l60.9-61.8c3.9-3.9,3.8-10.2-0.1-14.1
				c-3.9-3.9-10.2-3.8-14.1,0.1l-60.9,61.8C196.525,744.748,196.625,751.048,200.525,754.948z"
            />
            <path
                d="M335.225,754.948c2,1.9,4.5,2.9,7.1,2.9c2.6,0,5.1-0.9,7-2.9l61.8-61.8c3.9-3.9,3.9-10.2,0-14.1
				c-3.9-3.9-10.2-3.9-14.1,0l-61.8,61.8C331.325,744.748,331.325,751.048,335.225,754.948z"
            />
            <path
                d="M78.925,814.748c-3.8-3.9-10.2-4-14.1-0.1l-61.8,60.9c-3.9,3.8-4,10.2-0.1,14.1c1.9,2,4.5,3,7.1,3c2.5,0,5.1-0.9,7-2.9
				l61.8-60.9C82.725,825.048,82.725,818.648,78.925,814.748z"
            />
            <path
                d="M214.625,814.748c-3.8-3.9-10.2-4-14.1-0.1l-61.8,60.9c-3.9,3.8-4,10.2-0.1,14.1c1.9,2,4.5,3,7.1,3c2.5,0,5.1-0.9,7-2.9
				l61.8-60.9C218.425,825.048,218.425,818.648,214.625,814.748z"
            />
            <path
                d="M349.325,814.748c-3.9-3.9-10.2-3.9-14.1,0l-60.9,60.9c-3.9,3.9-3.9,10.2,0,14.1c2,1.9,4.5,2.9,7.1,2.9
				c2.5,0,5.1-1,7-2.9l60.9-60.9C353.225,824.948,353.225,818.648,349.325,814.748z"
            />
            <path
                d="M485.125,814.748c-3.8-3.9-10.2-4-14.1-0.1l-61.8,60.9c-3.9,3.8-4,10.2-0.1,14.1c1.9,2,4.5,3,7.1,3c2.5,0,5-0.9,7-2.9
				l61.8-60.9C488.925,825.048,489.025,818.648,485.125,814.748z"
            />
            <path
                d="M126.525,949.548l-61.8,61.8c-3.9,3.9-3.9,10.2,0,14.1c2,1.9,4.5,2.9,7.1,2.9c2.6,0,5.2-1,7-2.9l61.8-61.8
				c3.9-3.9,3.9-10.2,0-14.1C136.725,945.648,130.425,945.648,126.525,949.548z"
            />
            <path
                d="M261.325,949.548l-60.9,61.8c-3.9,3.9-3.8,10.2,0.1,14.1c1.9,1.9,4.5,2.9,7,2.9h0c2.6,0,5.2-1,7.1-3l60.9-61.8
				c3.9-3.9,3.8-10.2-0.1-14.1C271.525,945.548,265.225,945.648,261.325,949.548z"
            />
            <path
                d="M397.025,949.548l-61.8,61.8c-3.9,3.9-3.9,10.2,0,14.1c2,1.9,4.5,2.9,7.1,2.9c2.6,0,5.1-1,7-2.9l61.8-61.8
				c3.9-3.9,3.9-10.2,0-14.1C407.225,945.648,400.925,945.648,397.025,949.548z"
            />
        </g>
    </g>
);

const imageFittingSvg = (
    <>
        <path
            stroke="null"
            id="svg_2"
            d="m9.68361,10.28122c0,0.60521 0.48941,1.09375 1.09571,1.09375s1.09571,-0.48854 1.09571,-1.09375s-0.48942,-1.09375 -1.09571,-1.09375s-1.09571,0.48854 -1.09571,1.09375zm-3.28712,-1.09375c0.60629,0 1.09571,-0.48854 1.09571,-1.09375s-0.48942,-1.09375 -1.09571,-1.09375s-1.09571,0.48854 -1.09571,1.09375s0.48942,1.09375 1.09571,1.09375zm0.36524,3.28126c0,0.60521 0.48942,1.09375 1.09571,1.09375s1.09571,-0.48854 1.09571,-1.09375s-0.48942,-1.09375 -1.09571,-1.09375s-1.09571,0.48854 -1.09571,1.09375zm-3.28712,-1.09375c0.60629,0 1.09571,-0.48854 1.09571,-1.09375s-0.48942,-1.09375 -1.09571,-1.09375s-1.09571,0.48854 -1.09571,1.09375s0.48942,1.09375 1.09571,1.09375zm7.66994,2.91667l-8.57572,0l8.78756,-6.26356l-0.42367,-0.59063l-9.28428,6.61356l0,-6.32189c0,-0.40104 -0.32871,-0.72917 -0.73047,-0.72917s-0.73047,0.32813 -0.73047,0.72917l0,7.29169c0,0.40104 0.32871,0.72917 0.73047,0.72917l10.22659,0c0.40176,0 0.73047,-0.32813 0.73047,-0.72917c0,-0.40104 -0.32871,-0.72917 -0.73047,-0.72917z"
            clipRule="evenodd"
            fillRule="evenodd"
        />
        <text xmlSpace="preserve" textAnchor="start" fontFamily="sans-serif" fontSize="9.44322px" id="svg_3" y="5.3225346" x="5.1441765" strokeWidth="0" stroke="#000">
            xy
        </text>
    </>
);

const lineFittingSvg = (
    <>
        <path
            stroke="null"
            id="svg_2"
            d="m9.68361,10.28122c0,0.60521 0.48941,1.09375 1.09571,1.09375s1.09571,-0.48854 1.09571,-1.09375s-0.48942,-1.09375 -1.09571,-1.09375s-1.09571,0.48854 -1.09571,1.09375zm-3.28712,-1.09375c0.60629,0 1.09571,-0.48854 1.09571,-1.09375s-0.48942,-1.09375 -1.09571,-1.09375s-1.09571,0.48854 -1.09571,1.09375s0.48942,1.09375 1.09571,1.09375zm0.36524,3.28126c0,0.60521 0.48942,1.09375 1.09571,1.09375s1.09571,-0.48854 1.09571,-1.09375s-0.48942,-1.09375 -1.09571,-1.09375s-1.09571,0.48854 -1.09571,1.09375zm-3.28712,-1.09375c0.60629,0 1.09571,-0.48854 1.09571,-1.09375s-0.48942,-1.09375 -1.09571,-1.09375s-1.09571,0.48854 -1.09571,1.09375s0.48942,1.09375 1.09571,1.09375zm7.66994,2.91667l-8.57572,0l8.78756,-6.26356l-0.42367,-0.59063l-9.28428,6.61356l0,-6.32189c0,-0.40104 -0.32871,-0.72917 -0.73047,-0.72917s-0.73047,0.32813 -0.73047,0.72917l0,7.29169c0,0.40104 0.32871,0.72917 0.73047,0.72917l10.22659,0c0.40176,0 0.73047,-0.32813 0.73047,-0.72917c0,-0.40104 -0.32871,-0.72917 -0.73047,-0.72917z"
            clipRule="evenodd"
            fillRule="evenodd"
        />
        <text xmlSpace="preserve" textAnchor="start" fontFamily="sans-serif" fontSize="10px" id="svg_3" y="5.7571483" x="7.3132892" strokeWidth="0" stroke="#000">
            {" "}
            z
        </text>
    </>
);

const icons = {
    contour: contourSvg,
    center: centerSvg,
    regionList: regionListSvg,
    spatialProfiler: spatialProfilerSvg,
    spectralProfiler: spectralProfilerSvg,
    stokes: stokesSvg,
    spectralLineQuery: spectralLineQuerySvg,
    smoothing: profileSmoothingSvg,
    moments: momentGeneratorSvg,
    distanceMeasuring: distanceMeasuringSvg,
    cursor: cursorSvg,
    line: lineSvg,
    polyline: polylineSvg,
    pv: pvSvg,
    imageFitting: imageFittingSvg,
    lineFitting: lineFittingSvg,
    vectorOverlay: vectorOverlaySvg
};