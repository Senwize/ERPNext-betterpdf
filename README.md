## Better PDF

Better PDF generator uses NodeJS with puppeteer and headless-chrome to generate PDFs.

When the script `html2pdf/html2pdf.js` is called using two `-` as parameters (`./html2pdf.js - -`) it will read HTML from the STDIN and output the PDF on STDOUT. The BetterPDF frappé app overrides the `download_pdf` and `report_to_pdf` api methods and re-implements them to use the html2pdf script. So frappé or any other app (like ERPNext) is not touched. Removing BetterPDF will have your setup revert to the default PDF generation.

### Installing

The BetterPDF app will install the node dependencies automatically, but you will need to install any chromium dependencies. See the following URL on which packages are required: [Chrome headless doesn't launch on UNIX](https://github.com/puppeteer/puppeteer/blob/main/docs/troubleshooting.md#chrome-headless-doesnt-launch-on-unix)

For example on Ubuntu:

```bash
sudo apt-get install ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release wget xdg-utils 
```

Then get the BetterPDF app using bench:

```bash
bench get-app betterpdf https://github.com/Senwize/ERPNext-betterpdf
```

Lastly install the app to your site

```bash
bench --site erp.yoursite.com install-app betterpdf
```

### Uninstalling

```bash
bench --site erp.yoursite.com uninstall-app betterpdf
```

#### License

MIT
