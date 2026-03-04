# https://quera.org/problemset/136630?tab=description
# ---------------------------------------------------


def sort_dependencies(packages, package_name):
    visited = set()
    package_dependencies = []

    def dfs(pkg):
        if pkg in visited:
            return
        visited.add(pkg)

        # First process all dependencies
        for dependency in packages.get(pkg, []):
            dfs(dependency)

        # Then add the package itself (if it's not the starting package)
        if pkg != package_name:
            package_dependencies.append(pkg)

    dfs(package_name)
    return package_dependencies
