import re

with open('pom.xml', 'r') as f:
    pom = f.read()

# Insert distributionManagement
if '<distributionManagement>' not in pom:
    dist_mgmt = """
  <distributionManagement>
    <site>
      <id>local-site</id>
      <url>file://${user.dir}/target/site/deploy</url>
    </site>
  </distributionManagement>
"""
    pom = pom.replace('</repositories>', '</repositories>' + dist_mgmt)

# Insert maven-site-plugin with stage
if 'maven-site-plugin' not in pom:
    plugin = """
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-site-plugin</artifactId>
        <version>3.12.1</version>
        <inherited>false</inherited>
        <executions>
          <execution>
            <id>stage-for-local</id>
            <phase>site</phase>
            <goals>
              <goal>stage</goal>
            </goals>
            <configuration>
               <stagingDirectory>${user.dir}/target/staging</stagingDirectory>
            </configuration>
          </execution>
        </executions>
      </plugin>
"""
    pom = pom.replace('<plugins>', '<plugins>' + plugin)

with open('pom.xml', 'w') as f:
    f.write(pom)
