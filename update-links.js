const fs = require('fs');
const path = require('path');

const files = ['index.html', 'what-is-mip.html', 'guild.html', 'build-log.html', 'join.html'];
const basePath = '/miply-website/';

files.forEach(file => {
    const filePath = path.join(__dirname, file);
    if (!fs.existsSync(filePath)) {
        console.log(`File not found: ${file}`);
        return;
    }

    let content = fs.readFileSync(filePath, 'utf8');
    
    // Update navigation links
    content = content.replace(/href="\/what-is-mip\.html"/g, `href="${basePath}what-is-mip.html"`);
    content = content.replace(/href="\/guild\.html"/g, `href="${basePath}guild.html"`);
    content = content.replace(/href="\/build-log\.html"/g, `href="${basePath}build-log.html"`);
    content = content.replace(/href="\/join\.html"/g, `href="${basePath}join.html"`);
    content = content.replace(/href="\/home"/g, `href="${basePath}"`);
    content = content.replace(/href="\/what-is-mip"/g, `href="${basePath}what-is-mip.html"`);
    content = content.replace(/href="\/guild"/g, `href="${basePath}guild.html"`);
    content = content.replace(/href="\/build-log"/g, `href="${basePath}build-log.html"`);
    content = content.replace(/href="\/join"/g, `href="${basePath}join.html"`);
    
    // Update internal footer links
    content = content.replace(/href="\/what-is-mip\.html"/g, `href="${basePath}what-is-mip.html"`);
    content = content.replace(/href="\/guild\.html"/g, `href="${basePath}guild.html"`);
    content = content.replace(/href="\/build-log\.html"/g, `href="${basePath}build-log.html"`);
    content = content.replace(/href="\/join\.html"/g, `href="${basePath}join.html"`);
    
    fs.writeFileSync(filePath, content);
    console.log(`Updated ${file}`);
});

console.log('\nAll navigation links updated with base path: ' + basePath);