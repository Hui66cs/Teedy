import os
modules = ['docs-core', 'docs-web-common', 'docs-web']
for mod in modules:
    pom_path = f"{mod}/pom.xml"
    with open(pom_path, 'r') as f:
        pom = f.read()

    plugin_xml = f"""
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-site-plugin</artifactId>
        <configuration>
          <outputDirectory>${{maven.multiModuleProjectDirectory}}/target/site/{mod}</outputDirectory>
        </configuration>
      </plugin>
"""
    if 'maven-site-plugin' not in pom:
        if '<plugins>' in pom:
            pom = pom.replace('<plugins>', '<plugins>' + plugin_xml)
        else:
            pom = pom.replace('</build>', f'  <plugins>{plugin_xml}</plugins>\n  </build>')
        with open(pom_path, 'w') as f:
            f.write(pom)

